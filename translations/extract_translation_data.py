# TODO
"""
- Get unit tests set up for running of script (e.g. against different JSON, outputs etc)

- Get values from dict recursively instead of multiple nested loops?

- Think of better way to handle intermittent keys in get_conditional_text_for_container().

- Add/amend other team/best practice stuff that's been missed out.
"""

import json
import os
import sys

TEXT_SEPARATOR = "±"
OUTPUT_FILE_EXTENSION = "_translate.txt"


def get_text_for_container(container):

    extracted_text = []

    if isinstance(container, dict):
        for key in ['description', 'label', 'title']:
            value = container.get(key)

            if value is not None and value != '':
                extracted_text.append(value)

    elif isinstance(container, list):
        for value in container:
            extracted_text.append(value)

    return extracted_text


def get_text(data):
    translatable_text = []

    # Get header section text
    translatable_text.extend(get_text_for_container(data))
    translatable_text.extend(get_conditional_text_for_container(data))

    # Now build up translatable text from the nested dictionaries and lists
    for group in data['groups']:
        translatable_text.extend(get_text_for_container(group))

        for block in group['blocks']:
            translatable_text.extend(get_text_for_container(block))

            for section in block['sections']:
                translatable_text.extend(get_text_for_container(section))
                translatable_text.extend(get_conditional_text_for_container(section))

                for question in section['questions']:
                    translatable_text.extend(get_text_for_container(question))
                    translatable_text.extend(get_conditional_text_for_container(question))

                    for answer in question['answers']:
                        translatable_text.extend(get_text_for_container(answer))
                        translatable_text.extend(get_conditional_text_for_container(answer))

    return translatable_text


def get_conditional_text_for_container(container):
    extracted_text = []

    extracted_text.extend(get_introduction_text(container))
    extracted_text.extend(get_options_text(container))
    extracted_text.extend(get_guidance_text(container))
    extracted_text.extend(get_validation_text(container))

    return extracted_text


def get_validation_text(container):
    extracted_text = []
    if 'validation' in container:
        for value in container['validation']['messages'].values():
            extracted_text.append(value)

    return extracted_text


def get_guidance_text(container):
    extracted_text = []
    if 'guidance' in container:

        guidance_text = container['guidance']

        if isinstance(guidance_text, str):
            extracted_text.append(container['guidance'])
        else:
            for guidance in container['guidance']:
                extracted_text.extend(get_text_for_container(guidance))

                if 'list' in guidance:
                    extracted_text.extend(get_text_for_container(guidance['list']))

    return extracted_text


def get_options_text(container):
    extracted_text = []
    if 'options' in container:
        for options in container['options']:
            extracted_text.extend(get_text_for_container(options))

            if 'other' in options:
                extracted_text.extend(get_text_for_container(options['other']))

    return extracted_text


def get_introduction_text(container):
    extracted_text = []
    if 'introduction' in container:
        if 'description' in container['introduction']:
            extracted_text.append(container['introduction']['description'])

        if 'information_to_provide' in container['introduction']:
            for value in container['introduction']['information_to_provide']:
                extracted_text.append(value)

    return extracted_text


def sort_text(text_to_sort):
    sorted_text = list(text_to_sort)
    sorted_text.sort(key=len, reverse=True)

    return sorted_text


def remove_duplicates(text_with_duplicates):
    return set(text_with_duplicates)


def output_text_to_file(text_list, file_name):
    with open(file_name, 'w', encoding="utf8") as output_file:

        for line in text_list:
            output_file.write("%s" % line + TEXT_SEPARATOR + "\r\n")


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
    print()
    exit(0)


if __name__ == '__main__':

    json_file = sys.argv[1]
    output_directory = sys.argv[2]

    command_line_handler(json_file, output_directory)
