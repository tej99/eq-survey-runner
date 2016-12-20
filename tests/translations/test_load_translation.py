import unittest
from translations.load_translation_data import *
from mock import mock_open, patch


class LoadTranslationTest(unittest.TestCase):

    def test_strip_and_split_text(self):
        test_result = strip_and_split_text(['test1±test2'])
        self.assertEqual(test_result, ['test1', 'test2'])

    def test_replace_strings(self):
        test_replace = replace_strings(['test1', 'test2'])
        self.assertEqual(test_replace, 'test2')


if __name__ == '__main__':
    unittest.main()

