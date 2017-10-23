import unittest
from unittest import TestCase
from hamcrest import *
from yamlparser.yamlparser import Node


class YamlNodeConstructionTest(TestCase):
    def test_node_with_none_type(self):
        n = Node({})
        assert_that(n.type == "NoneType")

    def test_node_without_type(self):
        assert_that(calling(Node).with_args({"a": "b"}),
                    raises(ValueError, "no type attribute"))

    def test_node_profession(self):
        n = Node({"type": "profession", "name": "Coiffeur"})
        assert_that(n.type, is_("profession"))
        assert_that(n.name, is_("Coiffeur"))
        assert_that(hasattr(n, "text"), is_(False))

    def test_node_person(self):
        n = Node({"type": "person", "name": "John Doe"})
        assert_that(n.type, is_("TextNode"))
        assert_that(n.name, is_("John Doe"))
        assert_that(n.text, is_("John Doe"))

    def test_node_body_valid_subs(self):
        n = Node({"type": "body", "name": "10 Forward",
                  "sub": [{"type": "person", "name": "Hans"}]})
        assert_that(n.type, is_("body"))
        assert_that(n.name, is_("10 Forward"))

    def test_node_body_invalid_subs(self):
        args = {"type": "body", "name": "10 Forward",
                  "sub": [{"type": "error", "name": "Hacker"}]}
        assert_that(calling(Node).with_args(args),
                    raises(ValueError, "Type not allowed in subs"))

    def test_node_role_flag_valid(self):
        args = {"type": "role", "position": "Major", "name": "John Doe",
                  "flags": ["executive"]}
        n = Node(args)
        assert_that(n.type, is_("role"))
        assert_that(n.name, is_("John Doe"))
        assert_that(n.executive, is_(True))

    def test_node_role_flag_invalid(self):
        args = {"type": "role", "position": "Major", "name": "John Doe",
                "flags": ["error"]}
        assert_that(calling(Node).with_args(args),
                    raises(ValueError, "Flag not allowed"))

    def test_node_role_flag_valid_textnode(self):
        args = {"type": "role", "position": "Major", "name": "John Doe",
                  "flags": ["executive","is_text"]}
        n = Node(args)
        assert_that(n.type, is_("TextNode"))
        assert_that(n.name, is_("John Doe"))
        assert_that(n.executive, is_(True))
        assert_that(n.is_text, is_(True))
        assert_that(n.text, is_("Major: John Doe"))

if __name__ == '__main__':
    unittest.main()
