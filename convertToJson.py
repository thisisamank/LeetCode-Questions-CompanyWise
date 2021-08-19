import csv
import os
from os import listdir
from os.path import isfile, join

mypath = './questions/'

allFiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

with open('output.json', 'a') as outfile:
    outfile.write('[')
    for fileName in allFiles:
        with open(os.getcwd()+"/questions/"+fileName) as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                outfile.write(
                    '{"question_number" : "' + row[0] + '"' +
                    ',"title" : "' + row[1] + '"' +
                    ',"percent_solved" : "' + row[2] + '"' +
                    ',"difficulty_tag" : "' + row[3] + '"' +
                    ',"difficulty_score" : "' + row[4] + '"' +
                    ',"question_url" : "' + row[5] + '"' +
                    '},')
                outfile.write('\n')
    outfile.write(']')