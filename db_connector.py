#!/usr/bin/python
# -*- coding:utf-8 -*-

# TODO: Specify Docs of function, add Doc for File and variables
import sys
import json
from mariadb import Error, connect


# TODO: Add check for empty list, raise EmptyListError
# TODO: change output to real json object
def get_all_synonyms() -> str:
    """Return all synonyms

    ADD DESCRIPTION

    :return: JSON as string
    :raise
    """
    try:
        con = connect(
            host='127.0.0.1',
            port=3306,
            user="naouser",
            password="Asube-2015!",
            database="nao")
    except Error as e:
        print("Error connecting to MariaDB Platform: ", e)
        sys.exit(1)

    cur = con.cursor()
    cur.execute("SELECT synonym, id FROM synonyms ORDER BY id")
    syn_list = []
    for synonym, syn_id in cur:
        syn_list.append({'synonym': synonym, 'id': syn_id})
    json_str = json.dumps(syn_list)
    con.close()
    return json_str


# TODO: add checks for wrong returns, raise Error
# TODO: change output to real json object
def get_all_generic_terms() -> str:
    """Return all generic terms

    ADD DESCRIPTION

    :return: JSON as string
    """
    try:
        con = connect(
            host='127.0.0.1',
            port=3306,
            user="naouser",
            password="Asube-2015!",
            database="nao")
    except Error as e:
        print("Error connecting to MariaDB Platform: ", e)
        sys.exit(1)

    cur = con.cursor()
    cur.execute("SELECT id, generic_term FROM generic_terms ORDER BY id")
    gt_list = []
    for gt_id, generic_term in cur:
        gt_list.append({'id': gt_id, 'generic_term': generic_term})
    json_str = json.dumps(gt_list)
    con.close()
    return json_str


# TODO: add checks for wrong returns, raise error
# TODO: change output to real json object
def get_all_answers():
    """Return all answers

    ADD DESCRIPTION

    :return: JSON as string
    """
    try:
        con = connect(
            host='127.0.0.1',
            port=3306,
            user="naouser",
            password="Asube-2015!",
            database="nao")
    except Error as e:
        print("Error connecting to MariaDB Platform: ", e)
        sys.exit(1)
    cur = con.cursor()
    cur.execute("SELECT caseID, primary_keywords, secondary_keywords, answer FROM matching_table ORDER BY caseID")
    ans_list = []
    for case_id, primary_keywords, secondary_keywords, answer in cur:
        ans_list.append(
            {'caseID': case_id, 'primary_keywords': primary_keywords, 'secondary_keywords': secondary_keywords,
             'answer': answer})
    json_str = json.dumps(ans_list)
    con.close()
    return json_str


def get_all_keywords() -> list:
    try:
        con = connect(
            host='127.0.0.1',
            port=3306,
            user="naouser",
            password="Asube-2015!",
            database="nao")
    except Error as e:
        print("Error connecting to MariaDB Platform: ", e)
        sys.exit(1)
    cur = con.cursor()
    cur.execute("SELECT primary_keywords, secondary_keywords FROM matching_table")
    keywords = []
    for primary_keywords, secondary_keywords in cur:
        kwords = primary_keywords.split(",")
        for kword in kwords:
            keywords.append(kword)
        kwords = secondary_keywords.split(",")
        for kword in kwords:
            keywords.append(kword)
    return keywords


# TODO: add checks for wrong returns, raise Error
def get_generic_term(synonym: str) -> str:
    """Searchs for the generic term of a synonym.

    ADD DESCRIPTION

    :param synonym: String of the word for which the generic term should be found.
    :return: Returns the generic term as string if there is one for the synonym.
    :raise RASENError: Generic term is not in the database table.
    """
    try:
        con = connect(
            host='127.0.0.1',
            port=3306,
            user="naouser",
            password="Asube-2015!",
            database="nao")
    except Error as e:
        print("Error connecting to MariaDB Platform: ", e)
        sys.exit(1)

    # Get cursor
    cur = con.cursor()
    reqstr = f"SELECT id, synonym FROM synonyms WHERE synonym='{synonym}'"
    cur.execute(reqstr)
    synonym_id = None
    for (id, synonym) in cur:
        synonym_id = id
    if synonym_id is None:
        con.close()
        return None
    reqstr = f"SELECT generic_term, id FROM generic_terms WHERE id={synonym_id}"
    cur.execute(reqstr)
    gen_term = None
    for (generic_term, id) in cur:
        gen_term = generic_term
    con.close()
    return gen_term


# TODO: add check for wrong case_id, raise InvalidCaseIDError
def get_answer(case_id: int) -> str:
    """Returns the answer for case_id

    ADD DESCRIPTION

    :param case_id: Integer of the specific answer.
    :return: Returns the answer as string if there is one.
    :raise InvalidCaseIDError: case_id is not in the database table.
    """
    try:
        con = connect(
            host='127.0.0.1',
            port=3306,
            user="naouser",
            password="Asube-2015!",
            database="nao")
    except Error as e:
        print("Error connecting to MariaDB Platform: ", e)
        sys.exit(1)

    # Get cursor
    cur = con.cursor()
    reqstr = f"SELECT answer, caseID FROM matching_table WHERE caseID={case_id}"
    cur.execute(reqstr)
    ans = None
    for (answer, caseID) in cur:
        ans = answer
    con.close()
    return ans


def get_caseIDs_by_keywords(word: str):
    try:
        con = connect(
            host='127.0.0.1',
            port=3306,
            user="naouser",
            password="Asube-2015!",
            database="nao")
    except Error as e:
        print("Error connecting to MariaDB Platform: ", e)
        sys.exit(1)
    cur = con.cursor()
    reqstr = f"SELECT caseID, keywords FROM matching_table WHERE keywords LIKE '%{word}%'"
    cur.execute(reqstr)
    cID = []
    for (caseID, keywords) in cur:
        cID.append(caseID)
    if len(cID) == 0:
        con.close()
        return None
    con.close()
    return cID


def get_weight_of_keyword(keyword: str) -> float:
    try:
        con = connect(
            host='127.0.0.1',
            port=3306,
            user="naouser",
            password="Asube-2015!",
            database="nao")
    except Error as e:
        print("Error connecting to MariaDB Platform: ", e)
        sys.exit(1)
    cur = con.cursor()
    reqstr = f"SELECT weight FROM weights WHERE keyword='{keyword}'"
    cur.execute(reqstr)
    wgt = None
    for (weight) in cur:
        wgt = weight
    con.close()
    return wgt


def get_weights():
    try:
        con = connect(
            host='127.0.0.1',
            port=3306,
            user="naouser",
            password="Asube-2015!",
            database="nao")
    except Error as e:
        print("Error connecting to MariaDB Platform: ", e)
        sys.exit(1)
    cur = con.cursor()
    reqstr = f"SELECT keyword, weight FROM weights"
    cur.execute(reqstr)
    weights = []
    for keyword, weight in cur:
        weights.append({'keyword': keyword, 'weight': weight})
    json_str = json.dumps(weights)
    con.close()
    return json_str


# TODO: Add checks for arguments to catch wrong data
def insert_answers(case_id: int, primary_keywords: str, secondary_keywords: str, answer: str):
    """Insert data into matching table

    :param case_id: The id as integer of the specific answer.
    :param primary_keywords: Each primary keyword as string to identify the answer.
    :param secondary_keywords: Each secondary keyword as string to identify the answer.
    :param answer: The answer as string which will be said by nao.
    :return:
    """
    try:
        con = connect(
            host='127.0.0.1',
            port=3306,
            user="naouser",
            password="Asube-2015!",
            database="nao")
    except Error as e:
        print("Error connecting to MariaDB Platform: ", e)
        sys.exit(1)

    # Get cursor
    cur = con.cursor()
    cur.execute("INSERT INTO matching_table (caseID, primary_keywords, secondary_keywords, answer) VALUES (?, ?, ?, ?)",
                (case_id, primary_keywords, secondary_keywords, answer))
    con.commit()
    con.close()
    print("Answer inserted with case_id=" + str(case_id) + ", primary_keywords=" + primary_keywords +
          ", secondary_keywords=" + secondary_keywords + " and answer=" + answer)


# TODO: Add checks for arguments to catch wrong data
def insert_generic_terms(id: int, generic_term: str):
    """Insert data into generics terms table

    :param id: ID as integer of the specific generic term.
    :param generic_term: The generic term as string.
    :return:
    """
    try:
        con = connect(
            host='127.0.0.1',
            port=3306,
            user="naouser",
            password="Asube-2015!",
            database="nao")
    except Error as e:
        print("Error connecting to MariaDB Platform: ", e)
        sys.exit(1)

    # Get cursor
    cur = con.cursor()
    cur.execute("INSERT INTO generic_terms (id, generic_term) VALUES (?, ?)", (id, generic_term))
    con.commit()
    con.close()
    print("Generic term inserted with id=" + str(id) + " and generic_term=" + generic_term)


# TODO: Add checks for arguments to catch wrong data
def insert_synonyms(synonym: str, id: int):
    """Insert data into synonyms table

    :param synonym: Synonym as string.
    :param id: ID as integer which will represent the generic term.
    :return:
    """
    try:
        con = connect(
            host='127.0.0.1',
            port=3306,
            user="naouser",
            password="Asube-2015!",
            database="nao")
    except Error as e:
        print("Error connecting to MariaDB Platform: ", e)
        sys.exit(1)

    # Get cursor
    cur = con.cursor()
    cur.execute("INSERT INTO synonyms (synonym, id) VALUES (?, ?)", (synonym, id))
    con.commit()
    con.close()
    print("Synonym inserted with synonym=" + synonym + " and id=" + str(id))


def insert_weight(keyword: str, weight: float):
    try:
        con = connect(
            host='127.0.0.1',
            port=3306,
            user="naouser",
            password="Asube-2015!",
            database="nao")
    except Error as e:
        print("Error connecting to MariaDB Platform: ", e)
        sys.exit(1)

    # Get cursor
    cur = con.cursor()
    cur.execute("INSERT INTO weights (keyword, weight) VALUES (?, ?)", (keyword, weight))
    con.commit()
    con.close()
    print("keyword=" + keyword + " with weight=" + str(weight) + " inserted")

def clear_tables():
    """Clears all 4 tables in the database

    :return: no return
    """
    try:
        con = connect(
            host='127.0.0.1',
            port=3306,
            user="naouser",
            password="Asube-2015!",
            database="nao")
    except Error as e:
        print("Error connecting to MariaDB Platform: ", e)
        sys.exit(1)

    # Get cursor
    cur = con.cursor()
    cur.execute("DELETE FROM matching_table")
    cur.execute("DELETE FROM synonyms")
    cur.execute("DELETE FROM generic_terms")
    cur.execute("DELETE FROM weights")
    con.commit()
    con.close()

# def init_db_connection():
#     """Initialize Database Connection
#
#     Initializes the connection to the database with specific data.
#     """
#     try:
#         global conn
#         conn = connect(
#             host='127.0.0.1',
#             port=3306,
#             user="naouser",
#             password="Asube-2015!",
#             database="nao"
#         )
#     except Error as e:
#         print("Error connecting to MariaDB Platform: ", e)
#         sys.exit(1)
#
#     # Get cursor
#     global cur
#     cur = conn.cursor()
#     print("Database connection initialized!")


# def close_db_connection():
#     """Close Database Connection
#     """
#     conn.close()
#     print("Database connection closed!")
