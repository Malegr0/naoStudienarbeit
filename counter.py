#!/usr/bin/python
# -*- coding:utf-8 -*-
import db_connector


def count_ids(question: list) -> int:
    counter = None
    for word in question:
        keyword_weight = db_connector.get_weight_of_keyword(word)
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
    highest_count = None
    case_id = None
    i = 0
    if counter is None:
        return None
    while i < len(counter):
        print("Aktuell höchstes Gewicht" + str(counter[i].get("count")))
        print("Aktuell höchste Case ID" + str(counter[i].get("case_id")))
        if highest_count is None:
            highest_count = counter[i].get("count")
            case_id = counter[i].get("case_id")
        elif highest_count < counter[i].get("count"):
            highest_count = counter[i].get("count")
            case_id = counter[i].get("case_id")
        elif highest_count == counter[i].get("count"):
            t_case_id = check_for_higher_id(question, case_id, counter[i].get("case_id"))
            if t_case_id is not None:
                case_id = t_case_id
        i += 1
    return case_id


def check_for_higher_id(question: list, case_id: int, new_case_id: int) -> int:
    case_id_keywords = db_connector.get_primary_keywords_by_caseID(case_id)
    case_id_counter = 0
    new_case_id_keywords = db_connector.get_primary_keywords_by_caseID(new_case_id)
    new_case_id_counter = 0
    if case_id_keywords is None or new_case_id_keywords is None:
        return None
    for word in question:
        if word in case_id_keywords:
            case_id_counter += 1
        if word in new_case_id_keywords:
            new_case_id_counter += 1
    if case_id_counter >= new_case_id_counter:
        return case_id
    else:
        return new_case_id
