#!/usr/bin/python3
"""Module lists all states from `hbtn_0e_0_usa` DB."""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         password=argv[2],
                         database=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    list = cur.fetchall()
    for idx in range(len(list)):
        print(list[idx])
