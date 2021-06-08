import sys
from mariadb import Error, connect

# global variables
conn = None
cur = None


def get_all_synonyms():
    cur.execute("SELECT word, synonym FROM synonyms")
    list = []
    for word, synonym in cur:
        dictionary = {
            "word": word,
            "synonym": synonym
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
