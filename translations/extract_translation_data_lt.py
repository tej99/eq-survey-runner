# TODO
"""
- Get unit tests set up for running of script (e.g. against different JSON, outputs etc)
- Add/amend other team/best practice stuff that's been missed out.
"""
#
import json
import os
from sys import argv

TEXT_SEPARATOR = "|"
OUTPUT_FILE_EXTENSION = "_translate.txt"


def get_text_for_container(container):
    extracted_text = []

    for key in ['description', 'label', 'title']:

        value = container.get(key)

        if value is not None and value != '':
            extracted_text.append(value)

    return extracted_text


def get_text(data):
    translatable_text = []

    translatable_text.extend(get_header_text(data))

    # Now build up translatable text from the nested dictionaries and lists
    for group in data['groups']:
        translatable_text.extend(get_text_for_container(group))

        for block in group['blocks']:
            translatable_text.extend(get_text_for_container(block))

            for section in block['sections']:
                translatable_text.extend(get_text_for_container(section))

                for question in section['questions']:
                    translatable_text.extend(get_text_for_container(question))
                    translatable_text.extend(get_guidance_text_in_question(question))

                    for answer in question['answers']:
                        translatable_text.extend(get_text_for_container(answer))
                        translatable_text.extend(get_options_text_in_answer(answer))
                        translatable_text.extend(get_validation_text_in_answer(answer))
                        translatable_text.extend(get_guidance_text_in_answer(answer))

    return translatable_text


def get_guidance_text_in_answer(answer):
    extracted_text = []
    if 'guidance' in answer.keys():
        extracted_text.append(answer['guidance'])

    return extracted_text


def get_options_text_in_answer(answer):
    extracted_text = []
    if 'options' in answer.keys():  # Ensure key is available!
        for options in answer['options']:
            extracted_text.extend(get_text_for_container(options))

            if 'other' in options.keys():
                extracted_text.extend(get_text_for_container(options['other']))

    return extracted_text


def get_validation_text_in_answer(answer):
    extracted_text = []
    if 'validation' in answer.keys():
        for value in answer['validation']['messages']:
            extracted_text.append(value)

    return extracted_text


def get_guidance_text_in_question(question):
    extracted_text = []

    if 'guidance' in question.keys():
        for guidance in question['guidance']:
            extracted_text.extend(get_text_for_container(guidance))

            if 'list' in guidance.keys():
                for value in guidance['list']:
                    extracted_text.append(value)

    return extracted_text


def get_header_text(data):
    extracted_text = []

    extracted_text.extend(get_text_for_container(data))

    if 'introduction' in data.keys():

        if 'description' in data['introduction'].keys():
            extracted_text.append(data['introduction']['description'])

        if 'information_to_provide' in data['introduction'].keys():
            for value in data['introduction']['information_to_provide']:
                extracted_text.append(value)

    return extracted_text


def sort_text(text_to_sort):
    sorted_text = list(text_to_sort)
    sorted_text.sort(key=len, reverse=True)

    return sorted_text


def remove_duplicates(text_with_duplicates):
    return set(text_with_duplicates)


def output_text_to_file(text_list, file_name):
    with open(file_name, 'w', encoding="utf8") as test_file:

        for line in text_list:
            test_file.write("%s" % line + TEXT_SEPARATOR + line.upper() + "\r\n")
            # print("%s" % line + TEXT_SEPARATOR + line.upper())     # Output the list - this is just for testing! Please remove after!


def strip_directory_and_extension(file):
    file_basename = os.path.basename(file)
    file_name = os.path.splitext(file_basename)[0]

    return file_name


def create_output_file_name_with_directory(output_directory, json_file):
    file_name = strip_directory_and_extension(json_file)
    file_name_with_extension = file_name + OUTPUT_FILE_EXTENSION
    file_name_with_directory = os.path.join(output_directory, file_name_with_extension)

    return file_name_with_directory


def deserialise_json(json_file_to_deserialise):
    with open(json_file_to_deserialise, 'r', encoding="utf8") as json_data:
        try:
            data = json.load(json_data)
            return data

        except ValueError:
            print("Error decoding JSON. Please ensure file is in valid JSON format.")
            return None



def command_line_handler(json_file, output_directory):

    print('Creating list of translatable text from: ' + json_file)
    deserialised_json = deserialise_json(json_file)

    if deserialised_json is None:
        # error was encountered
        exit(1)

    text = get_text(deserialised_json)

    print('Removing duplicate text...')
    unique_text = remove_duplicates(text)
    sorted_text = sort_text(unique_text)

    print('Outputting text to file...')
    output_file_name = create_output_file_name_with_directory(output_directory, json_file)
    output_text_to_file(sorted_text, output_file_name)

    print('Finished successfully.')
    print()
    print('Translated text output: ' + output_file_name)
    exit(0)


if __name__ == '__main__':
    # json_file = argv[1]
    # output_directory = argv[2]
    json_file = "/Users/liamtoozer/projects/eq-survey-runner/app/data/census_household.json"
    output_directory = "/Users/liamtoozer/projects/eq-survey-runner/translations"

    command_line_handler(json_file, output_directory)
