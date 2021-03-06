#!/usr/bin/python
# -*- coding:utf-8 -*-

import json
import db_connector
import weighting


def import_data():
    db_connector.clear_tables()
    answers = json.load(open('database_files/answers.json'))
    generic_terms = json.load(open('database_files/generic_terms.json'))
    synonyms = json.load(open('database_files/synonyms.json'))
    for answer in answers:
        db_connector.insert_answers(answer["caseID"], answer["primary_keywords"], answer["secondary_keywords"],
                                    answer["answer"])
    for generic_term in generic_terms:
        db_connector.insert_generic_terms(generic_term["id"], generic_term["generic_term"])
    for synonym in synonyms:
        db_connector.insert_synonyms(synonym["synonym"], synonym["id"])
    weights = weighting.calculate_weight()
    for weight in weights:
        db_connector.insert_weight(weight["keyword"], weight["count"])
    return True

