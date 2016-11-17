# When finished, get rid of everything between these characters!!!
#!!!

import json

with open('/Users/liamtoozer/projects/eq-survey-runner/app/data/1_0112.json', 'r', encoding="utf8") as jsonData:
    data = json.load(jsonData)

    jsonData.close()


# All translatable text from first layer of file
def get_header_text():

  # The list of strings we're going to build up
  the_list = []

  the_list.append(data['title'])
  the_list.append(data['description'])
  the_list.append(data['introduction']['description'])

  for value in data['introduction']['information_to_provide']:
    the_list.append(value)

  return the_list


def is_text_present(text, key):
  return text.get(key) != None and text.get(key) != ''



# All text from 'blocks' with given keys
def get_blocks_text(keys):

  # The list of strings we're going to build up
  the_list = []

  for key in keys:

    for group in data['groups']:
        for block in group['blocks']:

          if is_text_present(block, key):
            the_list.append(block.get(key))

  return the_list



# All text from 'sections' with given keys
def get_sections_text(keys):

  # The list of strings we're going to build up
  the_list = []

  for key in keys:

    for group in data['groups']:
        for block in group['blocks']:
            for section in block['sections']:

                # Check we've actually found something
                if is_text_present(section, key):
                  the_list.append(section.get(key))

  return the_list




# All text from 'questions' with given keys
def get_questions_text(keys):

  # The list of strings we're going to build up
  the_list = []

  for key in keys:

    for group in data['groups']:
        for block in group['blocks']:
            for section in block['sections']:
                for question in section['questions']:

                  # Check we've actually found something
                  if is_text_present(question, key):
                    the_list.append(question.get(key))

  return the_list


# All text from 'answers' with given keys
def get_answers_text(keys):

  # The list of strings we're going to build up
  the_list = []

  for key in keys:

    for group in data['groups']:
        for block in group['blocks']:
            for section in block['sections']:
                for question in section['questions']:
                    for answer in question['answers']:

                      # Check we've actually found something
                      if is_text_present(answer, key):
                        the_list.append(answer.get(key))

  return the_list


# All text from 'messages' with given keys
def get_validation_message_text():

  # The list of strings we're going to build up
  the_list = []

  for group in data['groups']:
      for block in group['blocks']:
          for section in block['sections']:
              for question in section['questions']:
                  for answer in question['answers']:

                    if 'validation' in answer:  # Ensure key is available!

                      for key, value in answer['validation']['messages'].items():

                        if is_text_present(answer['validation']['messages'], key):
                          the_list.append(value)

  return the_list




# Wrapper function which generates the output file
def get_translatable_text():

  keys = [
    'description',
    'guidance',
    'label',
    'title'
  ]

  header_text = get_header_text()
  blocks_text = get_blocks_text(keys)
  sections_text = get_sections_text(keys)
  question_text = get_questions_text(keys)
  validation_text = get_validation_message_text()

  # Convert to set to remove all duplicates
  unique_text = set(header_text + blocks_text + sections_text + question_text + validation_text)

  # Convert back to list to sort
  sorted_list = list(unique_text)
  sorted_list.sort()

  return sorted_list




def output_to_file(text_list):

  # Output the list - this is just for testing! Please remove after!
  # for line in text_list:
  #   print("%s|" % line + line.upper())

  # Dump the output to a file
  test_file = open('test.txt', 'w', encoding="utf8")

  for line in text_list:
    test_file.write("%s|" % line + line.upper() + "\n")

  test_file.close()



def run():
  text = get_translatable_text()

  output_to_file(text)


### Entry point for entire script for now...
run()

























# print(json.dumps(data))
# print data





#     data["mime_type"] = 'something/test'
#
#     jsonData.seek(0)
#
#     target_file = open('small_new.json', 'w')
#
#     json_dump = json.dumps(data, indent=4, separators=(',', ': '))
#
#     target_file.write(json_dump)
#
#     #json_dump = json.dumps(data, indent=4, separators=(',', ': '))
#
# #with open("file.txt", "w") as att_file:
# #    att_file.write(data)


    # with open('data.json', 'w') as f:
    #     json.dump(data, f)

# Reading data back

#!!!


def get_all_values(d, depth):
  print("here")
  if depth == 1:
    for i in d.values():
      yield i
  else:
    for v in d.values():
      if isinstance(v, dict):
        for i in d.values(v, depth - 1):
          yield i

with open("/Users/liamtoozer/projects/eq-survey-runner/scripts/test.txt", "r") as file:

  """
  - Get a list of each line from the file to translate.
  - Search through the JSON file (dict) for any strings which match the left side of text from the file.
  - If a matching string is found, replace it with the right side of the text from the file.
  """

  lines = list(file)
  # print(lines)
  get_all_values(data, 0)



# for value in list1:
#     print(value),

  #
  # contents = file.read()
  #
  #
  # print(contents)







