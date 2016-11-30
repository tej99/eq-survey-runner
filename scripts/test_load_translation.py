import unittest
from collections import OrderedDict

import re
import os
import click
from click.testing import CliRunner
import json
from mock import mock_open, patch
from scripts.load_translation import deserialise_json


class TestLoadTranslation(unittest.TestCase):

# - User runs script - params: JSON_FILE    TRANSLATE_TEXT_FILE
#     def test_command_line_handler_args(self):
#         # test if given arguments are processed correctly
#         runner = CliRunner()
#         result = runner.invoke(command_line_handler, ['file_name.json', 'text_file.txt'])
#         self.assertEquals(result.output, "(TEST) Creating list of translatable text from: file_name.json\n")


# - Open and load the JSON file which needs to have text translated. Ensure order is retained.
    def test_deserialise_json(self):
      mock = mock_open(read_data='{"title": "Survey"}')
      with patch('load_translation.open', mock, create=True):
        deserialised_json_data = deserialise_json('sample.json')

        self.assertEqual(deserialised_json_data['title'], 'Survey')



#
#     def test_invalid_json_load_exception(self):
#       invalid_json_file_content = '"title": "Survey"}'
#       deserialise_json() tests
#
#     def test_deserialise_json_order(self):
#       json_file_content = '{"title": "Survey", "description": "Describe this"}'
#       deserialise_json tests



# - Open and load the translatable text file.
#     def test_open_translate_text_file(self):
#       text_file_content = 'Text from file|TEXT FROM FILE'
#       load_translated_text_file() tests
#


#     - Remove new line characters from the text file
#     def test_remove_line_breaks(self):
#         text = ["\nText with line breaks \r\n"]


#     - Separate the file into 2 columns (using the separator):
#           Column 1 - Text to find in the JSON file
#           Column 2 - Text to replace in the JSON file
#
# - For each section in the JSON file:
#       - If the value text on the current JSON line matches with a row in the translated text:
#           - Replace that text in the JSON file with the translated text row

# - Output the converted JSON into a new file.



if __name__ == '__main__':
    unittest.main()
