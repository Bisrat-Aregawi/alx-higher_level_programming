#!/usr/bin/python3
"""Module lists a record from `hbtn_0e_0_usa` DB.

From `states` table it searches for `state name` and returns the record that
matches it.
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         password=argv[2],
                         database=argv[3])

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{:s}'".format(argv[4])
    query += " ORDER BY states.id ASC"
    cur.execute(query)

    list = cur.fetchall()
    for idx in range(len(list)):
        print(list[idx])
