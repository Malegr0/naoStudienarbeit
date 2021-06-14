# TODO: Specify Docs of function, add Doc for File and variables
import sys
from mariadb import Error, connect

# global variables
conn = None
cur = None


# TODO: Add check for empty list, raise EmptyListError
def get_all_synonyms() -> list[dict]:
    """Return all synonyms

    ADD DESCRIPTION

    :return: Returns a list of dictionaries with all synonyms.
    :raise EmptyListError: emptyList
    """
    cur.execute("SELECT synonym, id FROM synonyms")
    list = []
    for synonym, synonym_id in cur:
        dictionary = {
            "synonym": synonym,
            "generic_term": synonym_id
        }
        list.append(dictionary)
    return list


# TODO: add checks for wrong returns, raise Error
def get_generic_term(synonym: str) -> str:
    """Searchs for the generic term of a synonym.

    ADD DESCRIPTION

    :param synonym: String of the word for which the generic term should be found.
    :return: Returns the generic term as string if there is one for the synonym.
    :raise RASENError: Generic term is not in the database table.
    """
    cur.execute("SELECT id FROM synonyms WHERE synonym=?", synonym)
    synonym_id = cur
    cur.execute("SELECT generic_terms FROM generic_terms WHERE id=?", synonym_id)
    generic_term = cur
    return generic_term


# TODO: add check for wrong case_id, raise InvalidCaseIDError
def get_answer(case_id: int) -> str:
    """Returns the answer for case_id

    ADD DESCRIPTION

    :param case_id: Integer of the specific answer.
    :return: Returns the answer as string if there is one.
    :raise InvalidCaseIDError: case_id is not in the database table.
    """
    cur.execute("SELECT answer FROM matching_table WHERE caseID=?", case_id)
    return cur


def get_all_caseID(keywords: list[str]) -> int:
    caseIDs = list[dict]
    for keyword in keywords:
        cur.execute("SELECT caseID FROM matching_table WHERE keywords=?", keyword)
        for caseID in cur:
            if check_case_id(caseID, caseIDs):
                pass
            else:
                elem = {
                    "caseID": caseID,
                    "count": 1
                }
                caseIDs.append(elem)


def check_case_id(case_id: int, case_ids: list[dict]) -> bool:
    for element in case_ids:
        if case_id == element["caseID"]:
            return True
    return False


# TODO: Add checks for arguments to catch wrong data
def insert_answers(case_id: int, keywords: str, answer: str):
    """Insert data into matching table

    :param case_id: The id as integer of the specific answer.
    :param keywords: Each keyword as string to identify the answer.
    :param answer: The answer as string which will be said by nao.
    :return:
    """
    cur.execute("INSERT INTO matching_table (caseID, keywords, answer) VALUES (?, ?, ?)", (case_id, keywords, answer))


# TODO: Add checks for arguments to catch wrong data
def insert_generic_terms(id: int, generic_term: str):
    """Insert data into generics terms table

    :param id: ID as integer of the specific generic term.
    :param generic_term: The generic term as string.
    :return:
    """
    cur.execute("INSERT INTO generic_terms (id, generic_term) VALUES (?, ?)", (id, generic_term))


# TODO: Add checks for arguments to catch wrong data
def insert_synonyms(synonym: str, id: int):
    """Insert data into synonyms table

    :param synonym: Synonym as string.
    :param id: ID as integer which will represent the generic term.
    :return:
    """
    cur.execute("INSERT INTO synonyms (synonym, id) VALUES (?, ?)", (synonym, id))


def init_db_connection():
    """Initialize Database Connection

    Initializes the connection to the database with spezific data.
    """
    try:
        global conn
        conn = connect(
            user="root",
            password="Asube-2019!",
            host="127.0.0.1",
            database="nao"
        )
    except Error as e:
        print("Error connecting to MariaDB Platform: ", e)
        sys.exit(1)

    # Get cursor
    global cur
    cur = conn.cursor()


def close_db_connection():
    """Close Database Connection
    """
    conn.close()
