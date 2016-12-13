import unittest
from translations.extract_translation_data import *
from mock import mock_open, patch


class ManipulateTranslationTest(unittest.TestCase):

    def test_strip_directory_and_extension(self):
        test_strip_dir_and_extension = strip_directory_and_extension('')
        self.assertEqual(test_strip_dir_and_extension, '')

    def test_create_output_file_name_with_directory(self):
        test_output_to_file_with_directory = create_output_file_name_with_directory('')
        self.assertEqual(test_output_to_file_with_directory, '')

    def test_deserialise_json(self):
        mock = mock_open(read_data='{"title": "Survey"}')
        with patch('builtins.open', mock, create=True):
            deserialised_json_data = deserialise_json('sample.json')
            self.assertEqual(deserialised_json_data['title'], 'Survey')

    def test_deserialise_json_raises_exception(self):
            mock = mock_open(read_data='{"title": "Survey"')
            with patch('builtins.open', mock, create=True):
                self.assertRaises(ValueError, deserialise_json('sample.json'))

if __name__ == '__main__':
    unittest.main()

