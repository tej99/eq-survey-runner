import json


with open('1_0112.json', 'r') as jsonData:
    data = json.load(jsonData)

    #jsonData.close()
    var = ''

##### Prints off everything in the title area

    var += data["title"] + '\n'

    var += data["description"] + '\n'

    var += data['introduction']['description'] + '\n'

    var += data['introduction']['information_to_provide'][0] + '\n'
    var += data['introduction']['information_to_provide'][1] + '\n'
    var += data['introduction']['information_to_provide'][2] + '\n'
    var += data['introduction']['information_to_provide'][3] + '\n'

    # if not data['groups']:
    #     print 'No Data!'
    # else:
    #     for rows in data['groups']:
    #         var += data['blocks']


    # for var1 in jsonData:
    #     for attribute, value in var1.iteritems():
    #       var += attribute, value


    # var += "\n".join(data['introduction']['information_to_provide'][0:])


##### Extract all data that can be translated

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

##### Prints off everything in 'groups > blocks > sections > questions > answers

##### prints section 1 (Reporting Period)

    # print(data['groups'][0]['blocks'][0]['sections'][0]['questions'][0]['answers'][0]['label'])
    # print(data['groups'][0]['blocks'][0]['sections'][0]['questions'][0]['answers'][0]['validation'])
    #
    # print(data['groups'][0]['blocks'][0]['sections'][0]['questions'][0]['answers'][1]['label'])
    # print(data['groups'][0]['blocks'][0]['sections'][0]['questions'][0]['answers'][1]['validation'])
    #
    # print(data['groups'][0]['blocks'][0]['sections'][0]['questions'][0]['description'])
    # print(data['groups'][0]['blocks'][0]['sections'][0]['questions'][0]['title'])

##### First sections part
##### Blocks == sections in the data


##### prints section 2 (Retail Turnover)

    # print(data['groups'][0]['blocks'][1]['sections'][0]['questions'][0]['answers'][0]['label'])
    # print(data['groups'][0]['blocks'][1]['sections'][0]['questions'][0]['answers'][0]['validation'])
    #
    # print(data['groups'][0]['blocks'][1]['sections'][0]['questions'][0]['description'])
    # print(data['groups'][0]['blocks'][1]['sections'][0]['questions'][0]['title'])
    #
    # print(data['groups'][0]['blocks'][1]['sections'][0]['title'])
    # print(data['groups'][0]['blocks'][1]['title'])


##### prints section 3 (Internet Sales)


    # print(data['groups'][0]['blocks'][2]['sections'][0]['questions'][0]['answers'][0]['label'])
    # print(data['groups'][0]['blocks'][2]['sections'][0]['questions'][0]['answers'][0]['validation'])
    #
    # print(data['groups'][0]['blocks'][2]['sections'][0]['questions'][0]['description'])
    # print(data['groups'][0]['blocks'][2]['sections'][0]['questions'][0]['title'])
    #
    # print(data['groups'][0]['blocks'][2]['sections'][0]['title'])
    # print(data['groups'][0]['blocks'][2]['title'])


##### prints section 4 (Changes in total retail turnover)

    # print(data['groups'][0]['blocks'][3]['sections'][0]['questions'][0]['answers'][0]['label'])
    # print(data['groups'][0]['blocks'][3]['sections'][0]['questions'][0]['answers'][0]['validation'])
    #
    # print(data['groups'][0]['blocks'][3]['sections'][0]['questions'][0]['description'])
    # print(data['groups'][0]['blocks'][3]['sections'][0]['questions'][0]['title'])
    #
    # print(data['groups'][0]['blocks'][3]['sections'][0]['title'])
    # print(data['groups'][0]['blocks'][3]['title'])


##### prints section 5 (Employees)

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


##### prints section 6 (Changes in employee figures)

    # print(data['groups'][0]['blocks'][5]['sections'][0]['questions'][0]['answers'][0]['label'])
    # print(data['groups'][0]['blocks'][5]['sections'][0]['questions'][0]['answers'][0]['validation'])
    #
    # print(data['groups'][0]['blocks'][5]['sections'][0]['questions'][0]['description'])
    # print(data['groups'][0]['blocks'][5]['sections'][0]['questions'][0]['title'])
    #
    # print(data['groups'][0]['blocks'][5]['sections'][0]['title'])
    # print(data['groups'][0]['blocks'][5]['title'])



##### prints last part ( main titles?)
    # print(data['groups'][0]['blocks'][0]['sections'][0]['title'])
    # print(data['groups'][0]['blocks'][0]['title'])


    # print(json.dumps(data))
    # print data


##### print variable + write to a file
    # print var
    #
    # test_file = open('test.txt', 'w')
    #
    # test_file.write(var)






##### try a for loop
##### prints off all data in groups

    # if data['groups'] == []:
    #     print 'No Data!'
    # else:
    #     for rows in data['groups']:
    #         print rows['blocks']




    # if data['groups'] == []:
    #     print 'No Data!'
    # else:
    #     for rows in data['groups']:
    #         for rows1 in data['blocks']:
    #             for rows2 in data['sections']:
    #                 for rows3 in data['questions']:
    #                     print rows3 in data['answers']





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
    
