#!/usr/bin/python3
"""Module lists a record from `hbtn_0e_0_usa` DB.

From `states` table it searches for `state name` and returns the record it
matches it. It also uses `%s` to capture the passed name safe from SQL
injection
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
    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC",
        (argv[4],)
    )

    list = cur.fetchall()
    for idx in range(len(list)):
        print(list[idx])
