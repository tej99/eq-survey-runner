import unittest
from translations.extract_translation_data import *
import os
import json
from mock import mock_open, patch


class ManipulateTranslationTest(unittest.TestCase):
    def test_output_text_to_file(self):
        test_output_to_file = remove_duplicates('')
        self.assertEqual(test_output_to_file, '')

    def test_strip_directory_and_extension(self):
        strip_dir_and_extension = remove_duplicates('')
        self.assertEqual(strip_dir_and_extension, '')

    def test_create_output_file_name_with_directory(self):
        test_output_to_file_with_directory = remove_duplicates('')
        self.assertEqual(test_output_to_file_with_directory, '')

    def test_deserialise_json(self):
        mock = mock_open(read_data='{"title": "Survey"}')
        with patch('builtins.open', mock, create=True):
            deserialised_json_data = deserialise_json('sample.json')
            self.assertEqual(deserialised_json_data['title'], 'Survey')

if __name__ == '__main__':
    unittest.main()

# @click.command()
