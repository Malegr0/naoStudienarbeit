import flask
from flask import request, jsonify

import db_connector

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


@app.route('/answers', methods=['POST'])
def post_answer():
    case_id = request.form.get('caseID')
    keywords = request.form.get('keywords')
    answer = request.form.get('answer')
    db_connector.insert_answers(case_id, keywords, answer)
    return 'OK'


@app.route('/genericTerms', methods=['POST'])
def post_generic_term():
    gn_id = request.form.get('id')
    generic_term = request.form.get('generic_term')
    db_connector.insert_generic_terms(gn_id, generic_term)
    return 'OK'


@app.route('/synonyms', methods=['POST'])
def post_synonyms():
    synonym = request.form.get('synonym')
    syn_id = request.form.get('id')
    db_connector.insert_synonyms(synonym, syn_id)
    return 'OK'
