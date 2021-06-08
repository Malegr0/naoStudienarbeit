import sys
from mariadb import Error, connect

# global variables
conn = None
cur = None


def get_all_synonyms():
    list = cur.execute("SELECT word, synonym FROM synonyms")
    print(list)
    #for word, synonym in cur:
        #TODO: result of sql request need to be added to a list


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
