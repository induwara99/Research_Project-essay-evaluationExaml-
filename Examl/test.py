import json

f = open('static/questions/lesson_1.json')
data = json.load(f)
for i in data['q']:
    print(i['question'])

# Closing file
f.close()
