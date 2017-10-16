import unittest
from unittest import TestCase
from hamcrest import *

class MarkdownParserTest(TestCase):
    def test_filename_doesnt_exist(self):
        print("*")
        assert_that(calling(get_filename).with_args([r'C:\a\b\c.csv']),
                    raises(IOError, "not a valid existing filename"))


if __name__ == '__main__':
    unittest.main()

# class MainClassTest(TestCase):
# from unittest.mock import MagicMock
# from unittest.mock import call
# from unittest.mock import patch
#     def test_filename_doesnt_exist(self):
#         print("*")
#         assert_that(calling(get_filename).with_args([r'C:\a\b\c.csv']),
#                     raises(IOError, "not a valid existing filename"))
#
#     def test_get_default_filename(self):
#         print("*")
#         assert_that(get_filename([]), is_(
#             r'C:\Users\ingo\Development\python\Requirements\resources\requirements.csv'))
#
#     def test_get_own_filename(self):
#         myFilename = r'C:\Users\ingo\Development\python\Requirements\resources\requirements.csv'
#         assert_that(get_filename([myFilename]), is_(myFilename))
#         print("*")
#
#     @patch('requirements.csvparser.main.Parser.parse')
#     def test_parser_call(self, mock_Parser_parse: MagicMock):
#         """
#         Checks if small csv with unicode chars is read correctly.
#         For good instructions for mocks and @patch  see
#         * https://blog.fugue.co/2016-02-11-python-mocking-101.html and of course
#         * https://docs.python.org/3/library/unittest.mock.html
#         """
#         print("*")
#         testfile = os.path.join(BASE_DIR, "resources", "test.csv")
#         main([testfile])
#
#         expected = [call(['a', 'b', 'c']), call(['', '', '']),
#                     call(['Test', 'ä,h,ß', 'أب'])]
#         assert_that(
#             mock_Parser_parse.call_args_list,
#             is_(expected))
#
#
# from requirements.csvparser.components.parser import *
# from requirements.core.hierarchy import Artefact
#
#
# class ParserTest(TestCase):
#     def test_parse_invalid_row(self):
#         invalid_entries = {
#             "Number of fields ": ["a", ""],
#             "Number of fields": ["", "b", "", ""],
#             "not of type 'String'": ["", True, ""],
#             " not of type 'String'": [0, "", ""],
#             "Only one of the fields should be filled": ["", "b", "c"],
#         }
#         parser = Parser()
#
#         for error_description, invalid_row in invalid_entries.items():
#             assert_that(calling(parser.parse_row).with_args(invalid_row),
#                         raises(ValueError, error_description))
#
#     def test_do_nothing_on_empty_row(self):
#         out = Parser()
#         assert_that(isinstance(out.parse_row(["", "", ""]), NullArtefact))
#
#     def test_transform_row_to_artefact(self):
#         out = Parser()
#         result: Artefact = out.parse_row(["a", "", ""])
#         assert_that(result.id, greater_than(0))
#
#     def test_field_parser_with_normal_field(self):
#         out = parse_cell_content("test")
#         assert_that(out["title"],is_("test"))
#         assert_that(out["role"],is_(None))
#         assert_that(out["tool"],is_(None))
#
#     def test_field_parser_with_role(self):
#         out = parse_cell_content("(bla) test")
#         assert_that(out["title"].strip(),is_("test"))
#         assert_that(out["role"],is_("bla"))
#         assert_that(out["tool"],is_(None))
#
#     def test_field_parser_with_role_and_tool(self):
#         out = parse_cell_content("(bla) test => ompf")
#         assert_that(out["title"].strip(),is_("test"))
#         assert_that(out["role"].strip(),is_("bla"))
#         assert_that(out["tool"].strip(),is_("ompf"))
#
#     def test_enrich(self):
#         tokens = {
#             "title": "mtitle",
#             "description": "mdescription",
#             "role": "mrole",
#             "tool": "mtool"
#         }
#         artefact = Epic()
#         out = Parser().enrich(artefact, tokens)
#         assert_that(artefact.title, is_("mtitle"))
#
#         artefact = Task()
#         out = Parser().enrich(artefact, tokens)
#         assert_that(artefact.title, is_("mtitle"))
#
#         artefact = Story()
#         out = Parser().enrich(artefact, tokens)
#         assert_that(artefact.title, is_("mtitle"))
#         assert_that(artefact.description, is_("mdescription"))
#         assert_that(artefact.role.title, is_("mrole"))
#         assert_that(artefact.tool.title, is_("mtool"))





