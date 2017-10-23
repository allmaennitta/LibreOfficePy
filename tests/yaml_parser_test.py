import unittest
from unittest import TestCase
from hamcrest import *
from yamlparser.yamlparser import YamlParser

class YamlParserTest(TestCase):
    def test_titled_empty_box(self):
        ou = """
---
-
  type: body
  name: Executive Board
  sub:
  - N.N
"""
        p = YamlParser()
        p.parseOrgaUnit(ou)
        assert_that(len(p.nodes), is_(1))
        assert_that(p.nodes[0].name, is_("Executive Board"))
        assert_that(len(p.nodes[0].nodes),is_(1))
        assert_that((p.nodes[0].nodes[0].type),is_("NoneType"))

    def test_titled_box_with_person(self):
        ou = """
---
-
  type: body
  name: Executive Board
  sub:
  - 
    type: person
    name: John Doe
  - 
    type: person
    name: N.N.
"""
        p = YamlParser()
        p.parseOrgaUnit(ou)
        assert_that(len(p.nodes), is_(1))
        assert_that(p.nodes[0].name, is_("Executive Board"))
        assert_that(p.nodes[0].nodes[0].text, is_("John Doe"))
        assert_that(p.nodes[0].nodes[1].text, is_("N.N."))

    def test_titled_box_with_person_and_textrole(self):
        ou = """
---
-
  type: body
  name: Executive Board
  sub:
  - 
    type: person
    name: John Doe
  - 
    type: person
    name: N.N.
  - 
    type: role
    position: General
    name: John Doe
    flags: ["is_text"]
"""
        p = YamlParser()
        p.parseOrgaUnit(ou)
        assert_that(len(p.nodes), is_(1))
        assert_that(p.nodes[0].name, is_("Executive Board"))
        assert_that(p.nodes[0].nodes[0].text, is_("John Doe"))
        assert_that(p.nodes[0].nodes[2].text, is_("General: John Doe"))

    def test_titled_box_with_textrole_and_noderole(self):
        ou = """
---
-
  type: body
  name: Executive Board
  sub:
  - 
    type: person
    name: John Doe
  - 
    type: person
    name: N.N.
  - 
    type: role
    position: General
    name: John Doe
    flags: ["is_text"]
  - 
    type: role
    position: Major
    name: John Doe    
"""
        p = YamlParser()
        p.parseOrgaUnit(ou)
        assert_that(len(p.nodes), is_(1))
        assert_that(p.nodes[0].name, is_("Executive Board"))
        assert_that(p.nodes[0].nodes[0].text, is_("John Doe"))
        assert_that(p.nodes[0].nodes[2].text, is_("General: John Doe"))
        assert_that(p.nodes[0].nodes[3].position, is_("Major"))

    def test_titled_box_with_teams_and_professions(self):
        ou = """
---
-
    type: department
    name: Research & Development
    sub:
    -
      type: role
      position: Director
      name: John Doe
    -
      type: team
      name: Foo
    -
      type: team
      name: Bar
    -
      type: profession
      name: Chemist for Process Engineering
    -
      type: profession
      name: CAD-Designer      
"""
        p = YamlParser()
        p.parseOrgaUnit(ou)
        assert_that(len(p.nodes), is_(1))
        assert_that(p.nodes[0].name, is_("Research & Development"))
        assert_that(p.nodes[0].nodes[1].text, is_("Foo"))
        assert_that(p.nodes[0].nodes[3].text, is_("Chemist for Process Engineering"))
if __name__ == '__main__':
    unittest.main()

