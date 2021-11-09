#!/usr/bin/python
# -*- coding:utf-8 -*-

# TODO: Implement algorithm for calculating weight
# TODO: Method with list as Input and list as Output
# TODO: Save distinct keywords from input in another list
# TODO: Output list as list of dictionaries (other output type)

# {Informatik, Studium, was, für, in, Informatik, HWR, wer, wo, Standort, Studium}
keyword = ['Informatik', 'Studium', 'was', 'für', 'in', 'Informatik', 'HWR', 'wer', 'wo', 'Standort', 'Studium']


def calculate_weight(keywords: list):
    weightings = []
    keywords_amount = len(keywords)

    for word in keywords:
        if len(weightings) == 0:
            dict_record = {"keyword": word, "count": 1}
            weightings.append(dict_record)
            continue
        else:
            i = 0
            while i < len(weightings):
                if word == weightings[i].get("keyword"):
                    weightings[i].update({"count": weightings[i].get("count") + 1})
                    continue
                i += 1
            dict_record = {"keyword": word, "count": 1}
            weightings.append(dict_record)
    print(weightings)
