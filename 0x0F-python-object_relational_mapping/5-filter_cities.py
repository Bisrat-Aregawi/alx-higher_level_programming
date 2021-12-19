#!/usr/bin/python3
"""Module takes state name as argument to list its cities.

Uses `hbtn_0e_4_usa` DB to filter out cities belonging to the state
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         password=argv[2],
                         database=argv[3])

    cur = db.cursor()
    cur.execute(
        "SELECT cities.name FROM states JOIN cities ON cities.state_id =\
        states.id WHERE states.name = %s ORDER BY cities.id", (argv[4],)
    )

    list = cur.fetchall()

    print(", ".join(city[0] for city in list))
