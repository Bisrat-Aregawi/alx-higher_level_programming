#!/usr/bin/python3
"""Module lists all cities from `hbtn_0e_4_usa` DB."""


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
        "SELECT cities.id, cities.name, states.name FROM cities JOIN states ON\
        cities.state_id = states.id ORDER BY cities.id ASC"
    )

    list = cur.fetchall()
    for idx in range(len(list)):
        print(list[idx])
