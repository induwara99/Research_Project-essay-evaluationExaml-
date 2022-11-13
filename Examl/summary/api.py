import flask
from flask import Flask, request, render_template
import json
import werkzeug
import summerise as s

app = Flask(__name__)


@app.route('/sum', methods=['GET', 'POST'])
def sum():
    data_file = request.files['file']
    filename = werkzeug.utils.secure_filename(data_file.filename)
    print("\nReceived File name : " + data_file.filename)
    data_file.save('upload/' + filename)

    text = ''
    with open('data/1.txt') as file:
        for line in file:
            text += line.rstrip()

    sum = s.summarize(text, 0.5)

    return json.loads('{ "respond" : "' + str(sum) + '"}')


if __name__ == "__main__":
    app.run(debug=True)
