#!/usr/bin/python3
""" Defines function to get cities by state"""


import MySQLdb
import sys

def cities_by_states(username, password, database_name):
    """ Function to find cities by state """
    try:
        db = MySQLdb.connect(host='localhost',
                             port=3306,
                             user=username,
                             passwd=password,
                             db=database_name)
        cursor = db.cursor()
        query = ("SELECT * FROM cities "
                 "ORDER BY cities.id ASC")
        cursor.execute(query)
        cities = cursor.fetchall()
        for city in cities:
            print(city)
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error: ", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Wrong format")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        cities_by_states(username, password, database_name)
