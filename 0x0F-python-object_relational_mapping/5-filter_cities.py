#!/usr/bin/python3
""" Defines function to filter cities"""


import MySQLdb
import sys


def filter_cities(username, password, database_name, state_name):
    """ Function to filter cities by state """
    try:
        db = MySQLdb.connect(host='localhost',
                             port=3306,
                             user=username,
                             passwd=password,
                             db=database_name)
        cursor = db.cursor()
        query = ("SELECT cities.name FROM cities "
                 "INNER JOIN states ON cities.state_id = states.id "
                 "WHERE states.name = %s "
                 "ORDER BY cities.id ASC")
        cursor.execute(query, (state_name,))
        cities = cursor.fetchall()
        print(cities)
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
        filter_cities(username, password, database_name, state_name)
