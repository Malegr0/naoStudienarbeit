import sys
from mariadb import Error, connect

# global variables
conn = None
cur = None


def get_all_synonyms():
    cur.execute("SELECT synonym, generic_term FROM synonyms")
    list = []
    for synonym, generic_term in cur:
        dictionary = {
            "synonym": synonym,
            "generic_term": generic_term
        }
        list.append(dictionary)
    print(list)



def init_db_connection():
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
    conn.close()
