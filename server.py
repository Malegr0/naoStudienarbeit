import flask
from flask import request, jsonify

app = flask.Flask(__name__)
# Change to False when using in production
app.config["DEBUG"] = True


def get_db_answer(question):
    return {
        "question": question,
        "answer": "Question received"
    }


@app.route('/', methods=['GET'])
def get_request():
    question = request.form['question']
    return jsonify(get_db_answer(question))
