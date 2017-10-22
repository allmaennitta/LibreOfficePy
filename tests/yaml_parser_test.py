import unittest
from unittest import TestCase
from hamcrest import *
from yamlparser.yamlparser import YamlParser

class MarkdownParserTest(TestCase):

    def test_titled_box(self):
        ou = """
---
organizational units:
-
  type: body
  name: Executive Board
  sub:
  - John Doe
  - N.N.
  """
        p = YamlParser()
        p.parseOrgaUnit(ou)
        assert_that(len(p.nodes), is_(1))
        assert_that(p.nodes[0].name, is_("Executive Board"))

    def test_titled_box_with_role(self):
        ou = """
---
-
  type: body
  name: Executive Board
  sub:
  - John Doe
  - N.N.
  - 
    type: role
    position: General
    name: John Doe
    flags: ["text"]
  """
        pass

    ou = """
    ---
    -
      type: executive role
      position: CEO
      name: Double Title
      sub:
      -
        type: role
        position: Text1/3
        name: John Doe
        flags: ["text"]
      -
        type: role
        position: Consigliere
        name: Text2/3
        flags: ["text"]
      -
        type: role
        position: Consigliere
        name: Text3/3
        flags: ["text"]
    """


    # def test_filename_doesnt_exist(self):
    #     assert_that(calling(get_filename).with_args([r'C:\a\b\c.csv']),
    #                 raises(IOError, "not a valid existing filename"))


if __name__ == '__main__':
    unittest.main()