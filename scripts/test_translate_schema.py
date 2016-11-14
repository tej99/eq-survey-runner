import json


with open('/Users/darrellcox/projects/eq-survey-runner/app/data/1_0112.json', 'r') as jsonData:
    data = json.load(jsonData)

    #jsonData.close()

# Prints off everything in the title area
def first_layer():
    # var = data['title']
    # var2 = data['description']
    # var3 = data['introduction']['description'] + '\n'

    var = ''
    var += data['title'] + '\n'
    var += data['description'] + '\n'
    var += data['introduction']['description'] + '\n'
    var += data['introduction']['information_to_provide'][0] + '\n'
    var += data['introduction']['information_to_provide'][1] + '\n'
    var += data['introduction']['information_to_provide'][2] + '\n'
    var += data['introduction']['information_to_provide'][3]
    print var

    # print var + '\n'
    # print var2 + '\n'
    # print var3 + '\n'
    #
    # for start in data['introduction']:
    #     print (data['information_to_provide'])

    # print variable + write to a file

    test_file = open('test.txt', 'w')

    test_file.write(var)

first_layer()


# def first_id():
#     output = []
#     for first in data:
#         for row in data[first]:
#             print(data[first][row])
#             output.append(data[first][row])





# try a for loop
# prints off all data in groups
# def groups_data():
#     if data['groups'] == []:
#         print 'No Data!'
#     else:
#         for rows in data['groups']:
#             print rows['blocks']

    # if data['groups'] == []:
    #     print 'No Data!'
    # else:
    # for group in data['groups']:


# All ID in blocks
def blocks_id():
    for group in data['groups']:
        for block in group['blocks']:
            #print (block.get('id'))
            print (block.get('title'))
            test_file = open('test.txt', 'a')
            test_file.write(block.get('title') + '\n')

# All ID in sections
def sections_id():
    for group in data['groups']:
        for block in group['blocks']:
            for section in block['sections']:
                #print (section.get('id'))
                print (section.get('title', 'description'))
                test_file = open('test.txt', 'a')
                test_file.write(section.get('title', 'description') + '\n')

# All ID in questions
def questions_id():
    for group in data['groups']:
        for block in group['blocks']:
            for section in block['sections']:
                for question in section['questions']:
                    #print (question.get('id'))
                    print (question.get('title', str('description')))
                    test_file = open('test.txt', 'a')
                    test_file.write(question.get('title', 'description') + '\n')

#All ID in answers
def answers_id():
    for group in data['groups']:
        for block in group['blocks']:
            for section in block['sections']:
                for question in section['questions']:
                    for answer in question['answers']:
                        #print (answer.get('id'))
                        print (answer.get('label'))
                        test_file = open('test.txt', 'a')
                        test_file.write(answer.get('label') + '\n')

# Prints ALL validation messages
def validation_messages():
    for group in data['groups']:
        for block in group['blocks']:
            for section in block['sections']:
                for question in section['questions']:
                    for answer in question['answers']:
                        for validate, value in answer['validation']['messages'].items():
                            print (value)
                            test_file = open('test.txt', 'a')
                            test_file.write(value + '\n')


blocks_id()
sections_id()
questions_id()
answers_id()
validation_messages()






# if not data['groups']:
#     print 'No Data!'
# else:
#     for rows in data['groups']:
#         var += data['blocks']


# for var1 in jsonData:
#     for attribute, value in var1.iteritems():
#       var += attribute, value


# var += "\n".join(data['introduction']['information_to_provide'][0:])


# Extract all data that can be translated

# print(data["mime_type"])
# print(data["questionnaire_id"])
# print(data["schema_version"])
# print(data["survey_id"])
# print(data["title"])
# print(data["description"])
# print(data["theme"])
# print(data["introduction"])
# print(data['introduction']['description'])
# print(data['introduction']['information_to_provide'][0:])
# print(data["eq_id"])

# prints section 1 (Reporting Period)

# print(data['groups'][0]['blocks'][0]['sections'][0]['questions'][0]['answers'][0]['label'])
# print(data['groups'][0]['blocks'][0]['sections'][0]['questions'][0]['answers'][0]['validation'])
#
# print(data['groups'][0]['blocks'][0]['sections'][0]['questions'][0]['answers'][1]['label'])
# print(data['groups'][0]['blocks'][0]['sections'][0]['questions'][0]['answers'][1]['validation'])
#
# print(data['groups'][0]['blocks'][0]['sections'][0]['questions'][0]['description'])
# print(data['groups'][0]['blocks'][0]['sections'][0]['questions'][0]['title'])


# prints section 2 (Retail Turnover)

# print(data['groups'][0]['blocks'][1]['sections'][0]['questions'][0]['answers'][0]['label'])
# print(data['groups'][0]['blocks'][1]['sections'][0]['questions'][0]['answers'][0]['validation'])
#
# print(data['groups'][0]['blocks'][1]['sections'][0]['questions'][0]['description'])
# print(data['groups'][0]['blocks'][1]['sections'][0]['questions'][0]['title'])
#
# print(data['groups'][0]['blocks'][1]['sections'][0]['title'])
# print(data['groups'][0]['blocks'][1]['title'])


# prints section 3 (Internet Sales)


# print(data['groups'][0]['blocks'][2]['sections'][0]['questions'][0]['answers'][0]['label'])
# print(data['groups'][0]['blocks'][2]['sections'][0]['questions'][0]['answers'][0]['validation'])
#
# print(data['groups'][0]['blocks'][2]['sections'][0]['questions'][0]['description'])
# print(data['groups'][0]['blocks'][2]['sections'][0]['questions'][0]['title'])
#
# print(data['groups'][0]['blocks'][2]['sections'][0]['title'])
# print(data['groups'][0]['blocks'][2]['title'])


# prints section 4 (Changes in total retail turnover)

# print(data['groups'][0]['blocks'][3]['sections'][0]['questions'][0]['answers'][0]['label'])
# print(data['groups'][0]['blocks'][3]['sections'][0]['questions'][0]['answers'][0]['validation'])
#
# print(data['groups'][0]['blocks'][3]['sections'][0]['questions'][0]['description'])
# print(data['groups'][0]['blocks'][3]['sections'][0]['questions'][0]['title'])
#
# print(data['groups'][0]['blocks'][3]['sections'][0]['title'])
# print(data['groups'][0]['blocks'][3]['title'])


# prints section 5 (Employees)

# print(data['groups'][0]['blocks'][4]['sections'][0]['questions'][0]['answers'][0]['label'])
# print(data['groups'][0]['blocks'][4]['sections'][0]['questions'][0]['answers'][0]['validation'])
#
# print(data['groups'][0]['blocks'][4]['sections'][0]['questions'][0]['answers'][1]['label'])
# print(data['groups'][0]['blocks'][4]['sections'][0]['questions'][0]['answers'][1]['validation'])
#
# print(data['groups'][0]['blocks'][4]['sections'][0]['questions'][0]['answers'][2]['label'])
# print(data['groups'][0]['blocks'][4]['sections'][0]['questions'][0]['answers'][2]['validation'])
#
# print(data['groups'][0]['blocks'][4]['sections'][0]['questions'][0]['answers'][3]['label'])
# print(data['groups'][0]['blocks'][4]['sections'][0]['questions'][0]['answers'][3]['validation'])
#
# print(data['groups'][0]['blocks'][4]['sections'][0]['questions'][0]['answers'][4]['label'])
# print(data['groups'][0]['blocks'][4]['sections'][0]['questions'][0]['answers'][4]['validation'])
#
# print(data['groups'][0]['blocks'][4]['sections'][0]['questions'][0]['description'])
# print(data['groups'][0]['blocks'][4]['sections'][0]['questions'][0]['title'])
#
# print(data['groups'][0]['blocks'][4]['sections'][0]['title'])
# print(data['groups'][0]['blocks'][4]['title'])


# prints section 6 (Changes in employee figures)

# print(data['groups'][0]['blocks'][5]['sections'][0]['questions'][0]['answers'][0]['label'])
# print(data['groups'][0]['blocks'][5]['sections'][0]['questions'][0]['answers'][0]['validation'])
#
# print(data['groups'][0]['blocks'][5]['sections'][0]['questions'][0]['description'])
# print(data['groups'][0]['blocks'][5]['sections'][0]['questions'][0]['title'])
#
# print(data['groups'][0]['blocks'][5]['sections'][0]['title'])
# print(data['groups'][0]['blocks'][5]['title'])



# prints last part ( main titles?)
# print(data['groups'][0]['blocks'][0]['sections'][0]['title'])
# print(data['groups'][0]['blocks'][0]['title'])


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

