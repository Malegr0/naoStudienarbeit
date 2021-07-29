#!/usr/bin/python
#-*- coding:utf-8 -*-

# TODO: Specify Docs of function, add Doc for File and variables
import sys
import json
from mariadb import Error, connect


# TODO: Add check for empty list, raise EmptyListError
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
            user="root",
            password="Asube-2019!",
            database="nao")
    except Error as e:
        print("Error connecting to MariaDB Platform: ", e)
        sys.exit(1)

    cur = con.cursor()
    cur.execute("SELECT synonym, id FROM synonyms")
    syn_list = []
    for synonym, syn_id in cur:
        syn_list.append({'synonym': synonym, 'id': syn_id})
    json_str = json.dumps(syn_list)
    con.commit()
    con.close()
    return json_str


#TODO: add checks for wrong returns, raise Error
def get_all_generic_terms() -> str:
    """Return all generic terms

    ADD DESCRIPTION

    :return: JSON as string
    """
    try:
        con = connect(
            host='127.0.0.1',
            port=3306,
            user="root",
            password="Asube-2019!",
            database="nao")
    except Error as e:
        print("Error connecting to MariaDB Platform: ", e)
        sys.exit(1)

    cur = con.cursor()
    cur.execute("SELECT id, generic_term FROM generic_terms")
    gt_list = []
    for gt_id, generic_term in cur:
        gt_list.append({'id': gt_id, 'generic_term': generic_term})
    json_str = json.dumps(gt_list)
    con.commit()
    con.close()
    return json_str


#TODO: add checks for wrong returns, raise Error
def get_all_answers() -> str:
    """Return all answers

    ADD DESCRIPTION

    :return: JSON as string
    """
    try:
        con = connect(
            host='127.0.0.1',
            port=3306,
            user="root",
            password="Asube-2019!",
            database="nao")
    except Error as e:
        print("Error connecting to MariaDB Platform: ", e)
        sys.exit(1)

    cur = con.cursor()
    cur.execute("SELECT caseID, keywords, answer FROM matching_table")
    ans_list = []
    for case_id, keywords, answer in cur:
        ans_list.append({'caseID': case_id, 'keywords': keywords, 'answer': answer})
    json_str = json.dumps(ans_list)
    con.commit()
    con.close()
    return json_str


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
            user="root",
            password="Asube-2019!",
            database="nao")
    except Error as e:
        print("Error connecting to MariaDB Platform: ", e)
        sys.exit(1)

    # Get cursor
    cur = con.cursor()
    cur.execute("SELECT id FROM synonyms WHERE synonym=?", synonym)
    synonym_id = cur
    cur.execute("SELECT generic_terms FROM generic_terms WHERE id=?", synonym_id)
    generic_term = cur
    con.commit()
    con.close()
    return generic_term


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
            user="root",
            password="Asube-2019!",
            database="nao")
    except Error as e:
        print("Error connecting to MariaDB Platform: ", e)
        sys.exit(1)

    # Get cursor
    cur = con.cursor()
    cur.execute("SELECT answer FROM matching_table WHERE caseID=?", case_id)
    con.commit()
    con.close()
    return cur


def get_answer_by_str(word: str):
    try:
        con = connect(
            host='127.0.0.1',
            port=3306,
            user="root",
            password="Asube-2019!",
            database="nao")
    except Error as e:
        print("Error connecting to MariaDB Platform: ", e)
        sys.exit(1)

    cur = con.cursor()
    cur.execute(f"SELECT caseID FROM matching_table where keywords LIKE '%{word}%'")
    return None


# TODO: Add checks for arguments to catch wrong data
def insert_answers(case_id: int, keywords: str, answer: str):
    """Insert data into matching table

    :param case_id: The id as integer of the specific answer.
    :param keywords: Each keyword as string to identify the answer.
    :param answer: The answer as string which will be said by nao.
    :return:
    """
    try:
        con = connect(
            host='127.0.0.1',
            port=3306,
            user="root",
            password="Asube-2019!",
            database="nao")
    except Error as e:
        print("Error connecting to MariaDB Platform: ", e)
        sys.exit(1)

    # Get cursor
    cur = con.cursor()
    cur.execute("INSERT INTO matching_table (caseID, keywords, answer) VALUES (?, ?, ?)", (case_id, keywords, answer))
    con.commit()
    con.close()
    print("Answer inserted with case_id=" + case_id + ", keywords=" + keywords + " and answer=" + answer)


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
            user="root",
            password="Asube-2019!",
            database="nao")
    except Error as e:
        print("Error connecting to MariaDB Platform: ", e)
        sys.exit(1)

    # Get cursor
    cur = con.cursor()
    cur.execute("INSERT INTO generic_terms (id, generic_term) VALUES (?, ?)", (id, generic_term))
    con.commit()
    con.close()
    print("Generic term inserted with id=" + id + " and generic_term=" + generic_term)


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
            user="root",
            password="Asube-2019!",
            database="nao")
    except Error as e:
        print("Error connecting to MariaDB Platform: ", e)
        sys.exit(1)

    # Get cursor
    cur = con.cursor()
    cur.execute("INSERT INTO synonyms (synonym, id) VALUES (?, ?)", (synonym, id))
    con.commit()
    con.close()
    print("Synonym inserted with synonym=" + synonym + " and id=" + id)

# def init_db_connection():
#     """Initialize Database Connection
#
#     Initializes the connection to the database with spezific data.
#     """
#     try:
#         global conn
#         conn = connect(
#             host='127.0.0.1',
#             port=3306,
#             user="root",
#             password="Asube-2019!",
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
