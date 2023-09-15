#!/usr/bin/python3
""" Defines function to list states with N"""

import sys
import MySQLdb


def list_states_with_n(username, password, database_name):
    """ Function to list states with N """
    try:
        db = MySQLdb.connect(host='localhost',
                             port=3306,
                             user=username,
                             passwd=password,
                             db=database_name)
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC "
            "COLLATE utf8mb4_bin"
        )
        states = cursor.fetchall()
        for state in states:
            print(state)
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error: ", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        pass
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        list_states_with_n(username, password, database_name)
