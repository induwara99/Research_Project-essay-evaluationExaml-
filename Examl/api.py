import flask

from flask import Flask, request, render_template
import json
import werkzeug
import cv2
import numpy as np
import db
import json
import nltk
from datetime import datetime, date, time, timedelta

import essay_nswer_grading.ontology as on


# import question_generator.new_mcq as question_gen

# essay_obj = on.SentenceSimilarity()

app = Flask(__name__)
# Initialize the flask App

db = db.DB()
current_user = ''

onotology_obj = on.SentenceSimilarity()


# page links
@app.route('/')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/past_paper_mcq')
def past_paper_mcq():
    return render_template('past_paper_mcq.html')


@app.route('/past_paper_2017')
def past_paper_2017():
    x = datetime.now() + timedelta(seconds=3600)
    y = x.strftime("%b %d, %Y %H:%M:%S")
    return render_template('past_paper_2017.html', date=y)


@app.route('/past_paper_2018')
def past_paper_2018():
    x = datetime.now() + timedelta(seconds=3600)
    y = x.strftime("%b %d, %Y %H:%M:%S")
    return render_template('past_paper_2018.html', date=y)


@app.route('/past_paper_2019')
def past_paper_2019():
    x = datetime.now() + timedelta(seconds=3600)
    y = x.strftime("%b %d, %Y %H:%M:%S")
    return render_template('past_paper_2019.html', date=y)


@app.route('/past_paper_2020')
def past_paper_2020():
    x = datetime.now() + timedelta(seconds=3600)
    y = x.strftime("%b %d, %Y %H:%M:%S")
    return render_template('past_paper_2020.html', date=y)


@app.route('/past_paper_essay')
def past_paper_essay():
    return render_template('past_paper_essay.html')


@app.route('/past_paper_2017_essay')
def past_paper_2017_essay():
    x = datetime.now() + timedelta(seconds=3600)
    y = x.strftime("%b %d, %Y %H:%M:%S")
    return render_template('past_paper_2017_essay.html', date=y)


@app.route('/past_paper_2018_essay')
def past_paper_2018_essay():
    x = datetime.now() + timedelta(seconds=3600)
    y = x.strftime("%b %d, %Y %H:%M:%S")
    return render_template('past_paper_2018_essay.html', date=y)


@app.route('/past_paper_2019_essay')
def past_paper_2019_essay():
    x = datetime.now() + timedelta(seconds=3600)
    y = x.strftime("%b %d, %Y %H:%M:%S")
    return render_template('past_paper_2019_essay.html', date=y)


@app.route('/past_paper_2020_essay')
def past_paper_2020_essay():
    x = datetime.now() + timedelta(seconds=3600)
    y = x.strftime("%b %d, %Y %H:%M:%S")
    return render_template('past_paper_2020_essay.html', date=y)


@app.route('/essay_grading', methods=['POST'])
def essay_grading():
    question_01 = request.json['question_01']
    question_01_real_answer = request.json['question_01_real_answer']
    question_01_given_answer = request.json['question_01_given_answer']

    question_02 = request.json['question_02']
    question_02_real_answer = request.json['question_02_real_answer']
    question_02_given_answer = request.json['question_02_given_answer']

    question_01_similarity, question_01_answer_key_list = onotology_obj.main(question_01_real_answer,
                                                                             question_01_given_answer)
    question_02_similarity, question_02_answer_key_list = onotology_obj.main(question_02_real_answer,
                                                                             question_02_given_answer)

    if question_01_similarity == float("inf"):
        question_01_similarity = 0.0

    if question_02_similarity == float("inf"):
        question_02_similarity = 0.0

    return_json = '['

    return_json += '{ "question_01" : "' + question_01 + '",  "question_01_real_answer" : "' + question_01_real_answer + '", "score": ' + str(
        question_01_similarity) + ', "key_points_01" :  ['

    for i, key in enumerate(question_01_answer_key_list):
        if i == len(question_01_answer_key_list) - 1:
            return_json += '"' + key + '"]},'
        else:
            return_json += '"' + key + '", '

    return_json += '{ "question_02" : "' + question_02 + '",  "question_02_real_answer" : "' + question_02_real_answer + '", "score": ' + str(
        question_02_similarity) + ', "key_points_02" :  ['

    for i, key in enumerate(question_02_answer_key_list):
        if i == len(question_02_answer_key_list) - 1:
            return_json += '"' + key + '"]}]'
        else:
            return_json += '"' + key + '", '

    print(return_json)

    return json.loads(return_json)


@app.route('/mind_map')
def mind_map():
    return render_template('mind_map.html')


@app.route('/mind_map_lesson_1')
def mind_map_lesson_1():
    return render_template('mind_map_lesson_1.html')


@app.route('/mind_map_lesson_2')
def mind_map_lesson_2():
    return render_template('mind_map_lesson_2.html')


@app.route('/mind_map_lesson_3')
def mind_map_lesson_3():
    return render_template('mind_map_lesson_3.html')


@app.route('/mind_map_lesson_4')
def mind_map_lesson_4():
    return render_template('mind_map_lesson_4.html')


@app.route('/q_generator')
def q_gen():
    return render_template('q_gen.html')


@app.route('/test_question_lesson_1')
def test_question_lesson_1():
    return_list = []
    f = open('static/questions/lesson_1.json')
    data = json.load(f)
    for i, j in enumerate(data['q']):
        # print(j['question'])
        # print(j['answer'])
        return_list.append([i, j['answer'], j['question']])

    # Closing file
    f.close()

    return render_template('test_question_lesson_1.html', question_list=return_list)


@app.route('/test_question_lesson_2')
def test_question_lesson_2():
    return_list = []
    f = open('static/questions/lesson_2.json')
    data = json.load(f)
    for i, j in enumerate(data['q']):
        # print(j['question'])
        # print(j['answer'])
        return_list.append([i, j['answer'], j['question']])

    # Closing file
    f.close()

    return render_template('test_question_lesson_2.html', question_list=return_list)


@app.route('/test_question_lesson_3')
def test_question_lesson_3():
    return_list = []
    f = open('static/questions/lesson_3.json')
    data = json.load(f)
    for i, j in enumerate(data['q']):
        # print(j['question'])
        # print(j['answer'])
        return_list.append([i, j['answer'], j['question']])

    # Closing file
    f.close()

    return render_template('test_question_lesson_3.html', question_list=return_list)


@app.route('/test_question_lesson_4')
def test_question_lesson_4():
    return_list = []
    f = open('static/questions/lesson_4.json')
    data = json.load(f)
    for i, j in enumerate(data['q']):
        # print(j['question'])
        # print(j['answer'])
        return_list.append([i, j['answer'], j['question']])

    # Closing file
    f.close()

    return render_template('test_question_lesson_4.html', question_list=return_list)


@app.route('/profile')
def profile():
    user = db.get_user_by_email(email=current_user)

    if len(user) < 1:
        return render_template('login.html')

    return render_template('profile.html', email=user[0].get_email(), name=user[0].get_name(), user_id=user[0].get_id())


# Actions
@app.route('/login_action', methods=['POST'])
def login_action():
    email = request.form['email']
    password = request.form['password']

    if db.login(email=email, password=password):
        global current_user
        current_user = email
        return render_template('home.html')
    else:
        return render_template('login.html', status='Username Or Password Invalid')


@app.route('/register_action', methods=['POST'])
def register_action():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    cpassword = request.form['cpassword']

    if password == cpassword:
        db.save_user(name=name, email=email, password=password)
        return render_template('login.html', status='Register Success')
    else:
        return render_template('register.html', status='Password did not match')


if __name__ == "__main__":
    app.run(debug=True)
