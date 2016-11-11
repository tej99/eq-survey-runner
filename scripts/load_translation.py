

text_file = open("/Users/darrellcox/projects/eq-survey-runner/app/data/test.txt","r")
list1 = text_file.readlines()

for value in list1:
    print ("%s") % (value),
