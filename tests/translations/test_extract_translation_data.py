import unittest
from translations.extract_translation_data import *
from mock import mock_open, patch


class ExtractTranslationTest(unittest.TestCase):
    def test_get_text_for_container_with_dict(self):
        result_text = get_text_for_container({"label": "Test"})
        self.assertEqual(result_text, ['Test'])

    def test_get_text_for_container_with_list(self):
        result_text = get_text_for_container(['Test1', 'Test2'])
        self.assertEqual(result_text, ['Test1', 'Test2'])

    def test_get_text_for_container_when_empty(self):
        result_text = get_text_for_container({})
        self.assertEqual(result_text, [])

    def test_get_text_for_container_unknown_type(self):
        result_text = get_text_for_container('')
        self.assertEqual(result_text, [])


    def test_get_introduction_text(self):
        container = {"introduction": {
                        "description": "Test1",
                        "information_to_provide": ["Test2"]
                        }}
        result_text = get_introduction_text(container)
        self.assertEqual(result_text, ['Test1', 'Test2'])

    def test_get_options_text(self):
        container = {"options": [
                        {"label": "Test1",
                         "other": {"label": "Test2"}
                        }]}
        result_text = get_options_text(container)
        self.assertEqual(result_text, ["Test1", "Test2"])

    def test_get_guidance_text(self):
        container = {"guidance": [{"label": "Test"}]}
        result_text = get_guidance_text(container)
        self.assertEqual(result_text, ["Test"])

    def test_get_validation_text(self):
        container = {"validation": {"messages": {"mandatory": "Message Test"}}}
        result_text = get_validation_text(container)
        self.assertEqual(result_text, ["Message Test"])

    def test_sort_text(self):
        result_text = sort_text({'A', 'Bb', 'Ccc'})
        self.assertEqual(result_text, ['Ccc', 'Bb', 'A'])

    def test_remove_duplicates(self):
        result_text = remove_duplicates({'Test', 'Test'})
        self.assertEqual(result_text, {'Test'})

if __name__ == '__main__':
    unittest.main()
