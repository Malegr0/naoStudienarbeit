#!/usr/bin/python
# -*- coding:utf-8 -*-

# TODO: Change keyword_weight value to come from method

import db_connector


def count_ids(question: list) -> int:
    counter = None
    for word in question:
        keyword_weight = Abfrage2(word)
        ids = db_connector.get_caseIDs_by_keywords(word)
        if ids is None:
            continue
        for case_id in ids:
            counter = check_list(counter, case_id, keyword_weight)
    return check_for_highest_id(question, counter)


def check_list(counter: list, case_id: int, weight: float) -> list:
    if counter is None:
        counter = [{"case_id": case_id, "count": weight}]
        return counter
    else:
        i = 0
        while i < len(counter):
            if case_id == counter[i].get("case_id"):
                counter[i].update({"count": counter[i].get("count") + weight})
                return counter
            i += 1
        counter.append({"case_id": case_id, "count": weight})
        return counter


def check_for_highest_id(question: list, counter: list) -> int:
    highest = None
    case_id = None
    possible_case_id = None
    i = 0
    if counter is None:
        return None
    while i < len(counter):
        if highest is None:
            highest = counter[i].get("count")
            case_id = counter[i].get("case_id")
        elif highest < counter[i].get("count"):
            highest = counter[i].get("count")
            case_id = counter[i].get("case_id")
        elif highest == counter[i].get("count"):
            possible_case_id = counter[i].get("case_id")
            case_id = Abfrage3(question, case_id, possible_case_id)
        i += 1
    return case_id
