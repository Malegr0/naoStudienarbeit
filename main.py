#!/usr/bin/python
#-*- coding:utf-8 -*-

import server
import spacy
import sentence_algorithm

nlp = spacy.load("de_core_news_sm")
detected_sentence = "Was kannst du mir über den Studiengang Informatik erzählen?"
doc = nlp(detected_sentence)
sentence_algorithm.sentence_detection(doc)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #db_connector.init_db_connection()
    server.app.run(host='0.0.0.0', port=5050)
    #db_connector.close_db_connection()
    print("Successfully executed!")

