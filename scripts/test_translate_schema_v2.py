# TODO
"""
1 - Make nested loops less horrendous. Use recursion instead?

2 - Ignore any text between '<' and '>' and '{' and '}'.

3 - Find a way to remove all hardcoding. Can these be held globally in a properties file?

4 - Get unit tests set up for running of script (e.g. against different JSON, outputs etc)

5 - Add/amend other team/best practice stuff that's been missed out.

6 - Will this be run from command line for now? Guard against different inputs.
"""


import json

TEXT_SEPARATOR = "|"

with open('/Users/liamtoozer/projects/eq-survey-runner/app/data/1_0112.json', 'r', encoding="utf8") as jsonData:
    data = json.load(jsonData)

    jsonData.close()


def is_text_present(text, key):
  return text.get(key) != None and text.get(key) != ''


# Wrapper function which generates the output file
def get_text():

  # The list of strings we're going to build up
  translatable_text = []

  # The list of keys we need to get text for
  keys = [
    'description',
    'guidance',
    'label',
    'title'
  ]

  # Get translatable text from 'header' in file
  translatable_text.append(data['title'])
  translatable_text.append(data['description'])
  translatable_text.append(data['introduction']['description'])

  for value in data['introduction']['information_to_provide']:
    translatable_text.append(value)


  # Now build up translatable text from the nested dictionaries and lists
  for key in keys:

    for group in data['groups']:
      for block in group['blocks']:
        if is_text_present(block, key):
          translatable_text.append(block.get(key))

        for section in block['sections']:
          if is_text_present(section, key):
            translatable_text.append(section.get(key))

          for question in section['questions']:
            if is_text_present(question, key):
              translatable_text.append(question.get(key))

            for answer in question['answers']:
                if is_text_present(answer, key):
                  translatable_text.append(answer.get(key))

                if 'validation' in answer:  # Ensure key is available!

                  for value in answer['validation']['messages'].values():
                    if is_text_present(answer['validation']['messages'], key):
                      translatable_text.append(value)

  return translatable_text


def get_translatable_text():

  text = get_text()
  text.sort()

  # Convert to set to remove all duplicates
  unique_text = set(text)

  # Convert back to list to sort
  sorted_translatable_text = list(unique_text)
  sorted_translatable_text.sort()

  # return sorted_list
  return sorted_translatable_text



def output_to_file(text_list):

  # Dump the output to a file
  with open('test.txt', 'w', encoding="utf8") as test_file:

    # Output the list - this is just for testing! Please remove after!
    for line in text_list:
      print("%s" % line + TEXT_SEPARATOR + line.upper())

    for line in text_list:
      test_file.write("%s" % line + TEXT_SEPARATOR + line.upper() + "\n")



def run():
  text = get_translatable_text()

  output_to_file(text)


### Entry point for entire script for now...
run()
