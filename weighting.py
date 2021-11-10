#!/usr/bin/python
# -*- coding:utf-8 -*-

# TODO: Implement algorithm for calculating weight
# TODO: Method with list as Input and list as Output

# {Informatik, Studium, was, für, in, Informatik, HWR, wer, wo, Standort, Studium}


def calculate_weight(keywords: list):
    weightings = []
    keywords_amount = len(keywords)
    for word in keywords:
        weightings = distinct_list(weightings, word)
    print(weightings)


def distinct_list(weightings: list, keyword: str) -> list:
    if len(weightings) == 0:
        dict_record = {"keyword": keyword, "count": 1}
        weightings.append(dict_record)
        return weightings
    else:
        i = 0
        while i < len(weightings):
            if keyword == weightings[i].get("keyword"):
                weightings[i].update({"count": weightings[i].get("count") + 1})
                return weightings
            i += 1
        dict_record = {"keyword": keyword, "count": 1}
        weightings.append(dict_record)
        return weightings
