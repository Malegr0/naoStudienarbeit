#!/usr/bin/python
# -*- coding:utf-8 -*-

import db_connector


# calculate weightings of distinct keywords from input list
# TODO: check if calculation of weighting is correct
def calculate_weight() -> list:
    keywords = db_connector.get_all_keywords()
    weightings = []
    keywords_amount = len(keywords)
    for word in keywords:
        weightings = distinct_list(weightings, word)
    i = 0
    while i < len(weightings):
        weightings[i]["count"] = 1 - (weightings[i]["count"] / keywords_amount)
        i += 1
    return weightings


# write distinct keywords with their count in a list and return
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
