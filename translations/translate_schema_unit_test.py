import unittest
import re
import os
import click
import json
from click.testing import CliRunner

def get_text_for_container(container):
    extracted_text = ''

    for key in ['description', 'guidance', 'label', 'title']:
        value = container.get(key)

    if value is not None and value != '':
        extracted_text += value

    return extracted_text


def get_text():
    data = {
        "title": "Survey",
        "description": "Describe this",
        "introduction": {
            "description": "Describe the inside of this",
            "information_to_provide": [
                "value of total retail turnover",
                "value of internet sales",
                "numbers of employees",
                "reasons for changes to figures"
            ]
        }
    }
    translatable_text1 = [data['title'], data['description'], data['introduction']['description']]
    print(translatable_text1)
    return translatable_text1


def get_text2():
    data = {
        "title": "Survey",
        "description": "Describe this",
        "introduction": {
            "description": "Describe the inside of this",
            "information_to_provide": [
                "value of total retail turnover",
                "value of internet sales",
                "numbers of employees",
                "reasons for changes to figures"
            ]
        }
    }
    translatable_text2 = get_text()

    for value in data['introduction']['information_to_provide']:
        translatable_text2.append(value)
    print(translatable_text2)
    return translatable_text2


def sort_text(text_to_sort):
    sorted_text = list(text_to_sort)
    sorted_text.sort(reverse=True)
    return sorted_text


def remove_duplicates(text_with_duplicates):
    return set(text_with_duplicates)


# def output_to_file(text_list):
#     with open('test.txt', 'w', encoding="utf8") as test_file:
#         for line in text_list:
#             test_file.write("%s" % line + '±' + line.upper() + "\n")


def data_manipulation(line):
    print(line)
    return "%s" % line + '±' + line.upper() + "\n"


def regular_expression(line):
    re_tester = re.split('({{.+?}})', line, maxsplit=1)
    return re_tester


def check_file_exists(file_name):
    if not os.path.isfile(file_name):
        print()
        some_file = 'JSON file ' + '\'' + file_name + '\'' + ' not found.'
        print(some_file)
        return some_file


def strip_directory_and_extension(file):

  file_basename = os.path.basename(file)
  file_name = os.path.splitext(file_basename)[0]

  return file_name


def create_output_file_name_with_directory(output_directory, json_file):

  file_name = strip_directory_and_extension(json_file)
  file_name_with_extension = file_name + ".translate.txt"
  file_name_with_directory = os.path.join(output_directory, file_name_with_extension)

  return file_name_with_directory


@click.command()
@click.argument('test_file_name')
def command_line_handler(test_file_name):
  click.echo('(TEST) Creating list of translatable text from: ' + test_file_name)



def deserialise_json(json_file_to_deserialise):
  with open(json_file_to_deserialise, 'r', encoding="utf8") as json_data:
    try:
      data = json.load(json_data)
      return data

    except ValueError:
      click.secho("Error decoding JSON. Please ensure file is valid JSON format.", fg=STDOUT_EXCEPTION)
      exit(1)


## Not certain how to unit test optional flag arguments with click?
# @click.command()
# @click.option('-o')
# def command_line_with_option(output_directory):
#   click.echo('(TEST) Creating list of translatable text from: ' + output_directory)



class TestTranslationSchema(unittest.TestCase):

    def test_init(self):
        self.assertTrue(True)

    def test_get_text_for_container(self):
        data = {
            "title": "Survey",
            "description": "Describe this",
            "introduction": {
                "description": "Describe the inside of this",
                "information_to_provide": [
                    "value of total retail turnover",
                    "value of internet sales",
                    "numbers of employees",
                    "reasons for changes to figures"
                ]
            }
        }
        this_text = get_text_for_container(data)
        self.assertEqual(this_text, 'Survey')

    def test_get_text1(self):
        test_getting = get_text()
        self.assertEqual(test_getting, ['Survey', 'Describe this', 'Describe the inside of this'])

    def test_get_text2(self):
        test_getting = get_text2()
        self.assertEqual(test_getting, ['Survey',
                                        'Describe this',
                                        'Describe the inside of this',
                                        'value of total retail turnover',
                                        'value of internet sales',
                                        'numbers of employees',
                                        'reasons for changes to figures'])

    def test_sort(self):
        test_sorting = sort_text('helloo')
        # takes out the string, removes duplicates and sorts in reverse
        self.assertEqual(test_sorting, ['o', 'o', 'l', 'l', 'h', 'e'])

    def test_remove_duplicates(self):
        test_duplication = remove_duplicates('aaaaaaaaa')
        self.assertEqual(test_duplication, {'a'})

    # def test_output(self):
    #     test_output_file = output_to_file('stuff in file')
    #     self.assertEquals(test_output_file, 'stuff in file')

    def test_data_manipulation(self):
        test_data = data_manipulation('Business Survey')
        self.assertEquals(test_data, 'Business Survey±BUSINESS SURVEY\n')

    def test_regex(self):
        # checks a string for anything between {{}} and splits
        something = regular_expression('start {{exercise.start_date|pretty_date}} end')
        self.assertEquals(something, ['start ', '{{exercise.start_date|pretty_date}}', ' end'])

### May need to change this now as the Click library is checking for this.
    def test_check_file_exists1(self):
        # tests if the file exists
        test_file1 = check_file_exists('some_file')
        self.assertEquals(test_file1, 'JSON file \'some_file\' not found.')

### May need to change this now as the Click library is checking for this.
    def test_check_file_exists2(self):
        # tests if the file exists
        test_file2 = check_file_exists('another_file')
        self.assertNotEquals(test_file2, 'JSON file \'some_file\' not found.')

    def test_strip_directory_and_extension(self):
        # tests if directory and extension is removed from file name
        full_file_name = strip_directory_and_extension("/directory/file_name.json")
        self.assertEquals(full_file_name, "file_name")

    def test_create_output_file_name_with_directory(self):
        # tests if a file name and directory is changed to an outputfile
        full_file_name = create_output_file_name_with_directory("/directory/test_directory/", "file_name.json")
        self.assertEquals(full_file_name, "/directory/test_directory/file_name.translate.txt")

    def test_command_line_handler_arg(self):
        # test if a given argument is processed correctly
        runner = CliRunner()
        result = runner.invoke(command_line_handler, ['file_name.json'])
        self.assertEquals(result.output, "(TEST) Creating list of translatable text from: file_name.json\n")

## Not certain how to unit test optional flag arguments with click?
    # def test_command_line_arg_with_option(self):
    #     # test if a given argument and option is processed correctly
    #     runner = CliRunner()
    #     result = runner.invoke(command_line_with_option, o="/test/directory/")
    #     self.assertEquals(result.output, "(TEST) Creating list of translatable text from: /test/directory/\n")

    # def test_deserialise_json(self):
    #   # test if a given json formatted file returns deserialised text
    #   test_json_content = '{"testkey": "testvalue"}'
    #   test_json_file = "test_json.json"






if __name__ == '__main__':
    unittest.main()