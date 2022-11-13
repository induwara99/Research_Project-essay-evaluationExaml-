import essay_nswer_grading.answer_grading as ag

correct_answer = 'data/correct.txt'
given_answer = 'data/given.txt'

correct_answer_text = ''
given_answer_text = ''

with open(correct_answer) as file:
    while (line := file.readline().rstrip()):
        correct_answer_text += line + ' '

with open(given_answer) as file:
    while (line := file.readline().rstrip()):
        given_answer_text += line + ' '

result = ag.compute_cosine_similarity(text1=correct_answer_text, text2=given_answer_text)

print('Question : explain heart?')
print('==========================')
print('correct answer : ' + correct_answer_text)
print('==========================')
print('given answer : ' + given_answer_text)
print('==========================')
print('result : ' + str(round(result * 100, 2)) + ' %')
