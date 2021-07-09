import flask
from flask import request, jsonify

import db_connector

app = flask.Flask(__name__)
# Change to False when using in production
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def get_request():
    return jsonify("This is the server of nao.")


@app.route('/answers', methods=['GET', 'POST'])
def answers():
    case_id = request.form.get('caseID')
    keywords = request.form.get('keywords')
    answer = request.form.get('answer')
    db_connector.insert_answers(case_id, keywords, answer)
    return 'OK'


@app.route('/genericTerms', methods=['GET', 'POST'])
def generic_terms():
    gn_id = request.form.get('id')
    generic_term = request.form.get('generic_term')
    db_connector.insert_generic_terms(gn_id, generic_term)
    return 'OK'


@app.route('/synonyms', methods=['GET', 'POST'])
def synonyms():
    if request.method == 'POST':
        synonym = request.form.get('synonym')
        syn_id = request.form.get('id')
        db_connector.insert_synonyms(synonym, syn_id)
        return 'OK'
    else:
        return db_connector.get_all_synonyms()
