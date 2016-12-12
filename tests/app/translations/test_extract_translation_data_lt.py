import unittest
from translations.extract_translation_data_lt import *
from mock import mock_open, patch

data = {
    "options": [
        {
            "label": "Label Test",
            "description": "Description Test"
        }
    ],
    "validation": {
        "messages": {
            "mandatory": "Message Test"
        }
    },
    "guidance": [
        {
            "label": "Guidance Test"
        }
    ],  "introduction": {
        "description": "Description Test",
        "information_to_provide": [
          "Introduction Test"
        ]
    }
}


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


    def test_get_conditional_text_for_container_with_dict(self):
        container = {"validation": {"messages": {"mandatory": "Test"}}}
        result_text = get_conditional_text_for_container(container)
        self.assertEqual(result_text, ['Test'])

    def test_get_conditional_text_for_container_when_empty(self):
        container = get_conditional_text_for_container({})
        self.assertEqual(container, [])


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









# test the same three with relevant data
    def test_get_options_text_in_answer(self):
        get_option_text = get_conditional_text_for_container(data)
        self.assertEqual(get_option_text, ['Yes'])

    def test_get_validation_text_in_answer(self):
        get_validation_text = get_conditional_text_for_container(data)
        self.assertEqual(get_validation_text, ['message here'])

    def test_get_guidance_text_in_question(self):
        get_guidance_text = get_conditional_text_for_container(data)
        self.assertEqual(get_guidance_text, ['guidance text'])

    # test with no data to show it can be handled
    def test_empty_dict_with_get_options_text_in_answer(self):
        get_option_text = get_options_text_in_answer({})
        self.assertEqual(get_option_text, [])

    def test_empty_dict_with_get_validation_text_in_answer(self):
        get_validation_text = get_validation_text_in_answer({})
        self.assertEqual(get_validation_text, [])

    def test_empty_dict_with_guidance_text_in_question(self):
        get_guidance_text = get_guidance_text_in_question({})
        self.assertEqual(get_guidance_text, [])


# test to get all translatable header data
    def test_get_header_text(self):

        schema_header_text = {
            "description": "test1",
            "label": "test2",
            "title": "test3",
            "introduction": {
                "description": "test4",
                "information_to_provide": [
                    "test5"
                ]
            }
        }

        get_all_translatable_header_text = get_header_text(schema_header_text)
        self.assertEqual(get_all_translatable_header_text, ['test1', 'test2', 'test3', 'test4', 'test5'])


if __name__ == '__main__':
    unittest.main()
