# TODO
"""
- Get unit tests set up for running of script (e.g. against different JSON, outputs etc)
- Add/amend other team/best practice stuff that's been missed out.
"""
#
import json
import click
import os

TEXT_SEPARATOR = "±"
OUTPUT_FILE_EXTENSION = "_translate.txt"
STDOUT_EXCEPTION = 'red'


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

    return translatable_text


def get_options_text_in_answer(answer):
    extracted_text = []
    if 'options' in answer:  # Ensure key is available!
        for options in answer['options']:
            extracted_text.extend(get_text_for_container(options))

            if 'other' in options:
                extracted_text.extend(get_text_for_container(options['other']))

    return extracted_text


def get_validation_text_in_answer(answer):
    extracted_text = []
    if 'validation' in answer:
        for value in answer['validation']['messages'].values():
            extracted_text.append(value)

    return extracted_text


def get_guidance_text_in_question(question):
    extracted_text = []
    if 'guidance' in question:
        for guidance in question['guidance']:
            extracted_text.extend(get_text_for_container(guidance))

            if 'list' in guidance:
                for value in guidance['list']:
                    extracted_text.append(value)

    return extracted_text


def get_header_text(data):
    extracted_text = []
    if 'description' in data.get('introduction'):
        extracted_text.append(data['introduction']['description'])

    if 'information_to_provide' in data.get('introduction'):
        for value in data['introduction']['information_to_provide']:
            extracted_text.append(value)
    extracted_text.extend(get_text_for_container(data))

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
            # Throw this exception back up the callstack instead of echo-ing with Click
            click.secho("Error decoding JSON. Please ensure file is valid JSON format.", fg=STDOUT_EXCEPTION)
            exit(1)


@click.command()
# @click.argument('json_file', required=True, type=click.Path(exists=True))
@click.argument('json_file', required=True, default="/Users/darrellcox/projects/eq-survey-runner/app/data/census_household.json", type=click.Path(exists=True))
@click.option('-o', '--output_directory', default=os.getcwd(),
              type=click.Path(exists=True), help='Specify directory for text output file.'
)
def command_line_handler(json_file, output_directory):
    """
Takes a JSON file and outputs all translatable text into
a separate text file in current directory (unless otherwise
specified with '--output_directory' or '-o' option).
Parameters: \n
\tJSON_FILE - JSON file in the current path or in a fully-qualified path.
    """

    click.echo('Creating list of translatable text from: ' + json_file)
    deserialised_json = deserialise_json(json_file)
    text = get_text(deserialised_json)

    click.echo('Removing duplicate text...')
    unique_text = remove_duplicates(text)
    sorted_text = sort_text(unique_text)

    click.echo('Outputting text to file...')
    output_file_name = create_output_file_name_with_directory(output_directory, json_file)
    output_text_to_file(sorted_text, output_file_name)

    click.echo('Finished successfully.')
    click.echo()
    click.echo('Translated text output: ' + output_file_name)
    exit(0)


if __name__ == '__main__':
    command_line_handler()