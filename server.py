#!/usr/bin/python
#-*- coding:utf-8 -*-

import flask
import spacy
from flask import request, jsonify

import db_connector
import sentence_algorithm

app = flask.Flask(__name__)
# Change to False when using in production
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def get_request():
    question = request.form.get('question')
    if question is None:
        return jsonify("This is the server of nao.")
    nlp = spacy.load("de_core_news_sm")
    doc = nlp(question)
    found_words = sentence_algorithm.sentence_detection(doc)
    i = 0
    while i < len(found_words):
        wd = db_connector.get_generic_term(found_words[i])
        if wd is None:
            continue
        found_words[i] = wd
        i += 1
    return jsonify(found_words)


@app.route('/answers', methods=['GET', 'POST'])
def answers():
    if request.method == 'POST':
        case_id = request.form.get('caseID')
        keywords = request.form.get('keywords')
        answer = request.form.get('answer')
        db_connector.insert_answers(case_id, keywords, answer)
        return 'OK'
    else:
        return db_connector.get_all_answers()


@app.route('/genericTerms', methods=['GET', 'POST'])
def generic_terms():
    if request.method == 'POST':
        gn_id = request.form.get('id')
        generic_term = request.form.get('generic_term')
        db_connector.insert_generic_terms(gn_id, generic_term)
        return 'OK'
    else:
        return db_connector.get_all_generic_terms()


@app.route('/synonyms', methods=['GET', 'POST'])
def synonyms():
    if request.method == 'POST':
        synonym = request.form.get('synonym')
        syn_id = request.form.get('id')
        db_connector.insert_synonyms(synonym, syn_id)
        return 'OK'
    else:
        return db_connector.get_all_synonyms()
