#!/usr/bin/python3

import sys
import MySQLdb


def find_state(username, password, database_name, state_name):
    try:
        db = MySQLdb.connect(host='localhost',
                             port=3306,
                             user=username,
                             passwd=password,
                             db=database_name)
        cursor = db.cursor()
        query = ("SELECT * FROM states "
                 "WHERE name = '{}' ORDER BY states.id ASC").format(state_name)
        cursor.execute(query)
        states = cursor.fetchall()
        for state in states:
            print(state)
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error: ", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Wrong format")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        state_name = sys.argv[4]
        find_state(username, password, database_name, state_name)
