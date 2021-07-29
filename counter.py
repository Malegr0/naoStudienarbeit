#!/usr/bin/python
# -*- coding:utf-8 -*-

import db_connector


def count_ids(question: list) -> int:
    counter = None
    for word in question:
        ids = db_connector.get_answer_by_str(word)
        # TODO: add check for empty set
        for case_id in ids:
            counter = check_list(counter, case_id)
    return check_for_highest_id(counter)


def check_list(counter: list, case_id: int) -> list:
    if counter is None:
        counter = [{"case_id": case_id, "count": 1}]
        return counter
    else:
        i = 0
        while i < len(counter):
            if case_id == counter[i].get("case_id"):
                counter[i].update({"count": counter[i].get("count") + 1})
                return counter
            i += 1
        counter.append({"case_id": case_id, "count": 1})
        return counter


def check_for_highest_id(counter: list) -> int:
    highest = None
    case_id = None
    i = 0
    while i < len(counter):
        if highest is None:
            highest = counter[i].get("count")
            case_id = counter[i].get("case_id")
        elif highest < counter[i].get("count"):
            highest = counter[i].get("count")
            case_id = counter[i].get("case_id")
        i += 1
    return case_id
