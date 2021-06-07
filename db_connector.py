import sys

import mariadb

# global variables
conn = None
cur = None


def init_db_connection():
    try:
        global conn
        conn = mariadb.connect(
            user="root",
            password="Asube-2019!",
            host="127.0.0.1",
            database="nao"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get cursor
    global cur
    cur = conn.cursor()


def close_db_connection():
    conn.close()
