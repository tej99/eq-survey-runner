# TODO
"""
- Find a way to remove all hardcoding. Can these be held globally in a properties file?

- Get unit tests set up for running of script (e.g. against different JSON, outputs etc)

- Add/amend other team/best practice stuff that's been missed out.

- Will this be run from command line for now? Guard against different inputs.
"""

import json
import os
import click

TEXT_SEPARATOR = "±"
SCHEMA_DIR = os.path.expanduser('~') + "/projects/eq-survey-runner/app/data/"
OUTPUT_DIR = os.path.expanduser('~') + "/OUTPUTS"

print(os.path.expanduser('~'))

def get_text_for_container(container):
  # extracted_text = []
  extracted_text = ''

  for key in ['description', 'guidance', 'label', 'title']:

    value = container.get(key)

    if value is not None and value != '':
        # extracted_text.append(value)
      extracted_text += value

  return extracted_text


# Builds and returns a list of translatable text from JSON file
def get_text(json_file_to_deserialise):

  # Get the JSON file
  with open(json_file_to_deserialise, 'r', encoding="utf8") as json_data:
    data = json.load(json_data)

  # Create the list of strings we're going to build up and assign 'header' text first
  translatable_text = [data['title'], data['description'], data['introduction']['description']]

  for value in data['introduction']['information_to_provide']:
    translatable_text.append(value)


  # Now build up translatable text from the nested dictionaries and lists
  for group in data['groups']:
    for block in group['blocks']:
      translatable_text.append(get_text_for_container(block))

      for section in block['sections']:
        translatable_text.append(get_text_for_container(section))

        for question in section['questions']:
          translatable_text.append(get_text_for_container(question))

          for answer in question['answers']:
            translatable_text.append(get_text_for_container(answer))

            if 'validation' in answer:  # Ensure key is available!

              for value in answer['validation']['messages'].values():
                translatable_text.append(value)

  return translatable_text


def sort_text(text_to_sort):

  # Convert to set to remove all duplicates
  unique_text = set(text_to_sort)

  # Convert back to list to sort
  sorted_translatable_text = list(unique_text)
  sorted_translatable_text.sort(reverse=True)

  return sorted_translatable_text


def output_to_file(text_list):

  # Dump the output to a file
  with open('test.txt', 'w', encoding="utf8") as test_file:

    # Output the list - this is just for testing! Please remove after!
    for line in text_list:
      print("%s" % line + TEXT_SEPARATOR + line.upper())

    for line in text_list:
      test_file.write("%s" % line + TEXT_SEPARATOR + line.upper() + "\n")





# @click.command()
# @click.argument('json_file', type=click.Path(exists=True))
# def main(json_file):
#   """
#   This script takes a JSON schema file and outputs all translatable text into
#   a separate text file.
#   """
#   click.echo("JSON file '" + json_file + "'provided")
#
#   # json_file = SCHEMA_DIR + '1_0112.json'
#
#   click.echo('Creating list of translatable text from ' + json_file)
#   text = get_text(json_file)
#
#   click.echo('Making list unique...')
#   # unique_text = remove_duplicates(text)
#
#   click.echo('Sorting list...')
#   # sorted_text = sort_text(unique_text)
#   sorted_text = sort_text(text)
#
#   click.echo('Outputting list into file...')
#   output_to_file(sorted_text)
#
#   click.echo('Script complete.\nOutput of translated text: ' + "OUTPUT TEXT FILE LOCATION")
#
#
# if __name__ == '__main__':
#     main()



file = SCHEMA_DIR + '1_0112.json'

text = get_text(file)

sorted_text = sort_text(text)

output_to_file(sorted_text)





# def usage():
#     print()
#     print('Usage: python ' + os.path.basename(__file__) + ' <json_schema_file_name>')
#     exit(1)
#
#
# def check_file_exists(file_name):
#
#     if not os.path.isfile(file_name):
#       print()
#       print('JSON file ' + '\'' + file_name + '\'' + ' not found.')
#       exit(2)
