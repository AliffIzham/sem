import sqlite3

def convert(k):
    return ''.join(k).split()


def create_table():
    conn = sqlite3.connect("tracking.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE infos(
    track_num_in text,
    date_in text,
    date_out text,
    status text)
    """)
    print("Table created")

    conn.commit()
    conn.close()


def add_one():
    conn = sqlite3.connect("tracking.db")
    c = conn.cursor()

    track_in = input("Tracking in: ")
    date_in = input("Date in: ")
    date_out = input("Date out: ")
    status = input("Status: ")

    c.execute("INSERT INTO infos VALUES (?,?,?,?)", (track_in, date_in, date_out, status))
    print("Element added successfully")

    conn.commit()
    conn.close()


def show_all():
    conn = sqlite3.connect("tracking.db")
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM infos")

    items = c.fetchall()
    for item in items:
        print(item)

    conn.commit()
    conn.close()


def show_one():
    conn = sqlite3.connect("tracking.db")
    c = conn.cursor()

    find = input("Enter tracking number: ")
    j = convert(find)

    c.execute("SELECT * FROM infos WHERE track_num_in = ?", j)

    item = c.fetchall()
    print(item)

    conn.commit()
    conn.close()


def show_one_display(k, f):
    conn = sqlite3.connect("tracking.db")
    c = conn.cursor()

    c.execute("SELECT * FROM infos")

    items = c.fetchall()
    for item in items:
        if item[0] == k:
            conn.commit()
            conn.close()
            return item[f]

def check(k):
    conn = sqlite3.connect("tracking.db")
    c = conn.cursor()

    c.execute("SELECT * FROM infos")

    items = c.fetchall()
    for item in items:
        if item[0] == k:
            conn.commit()
            conn.close()
            return True


def update():
    conn = sqlite3.connect("tracking.db")
    c = conn.cursor()

    num_updated = input("Enter item to be updated (track in): ")

    date_in_updated = input("Date in: ")
    date_out_updated = input("Date out: ")
    status_updated = input("Status: ")

    print(date_in_updated)

    c.execute("""UPDATE infos SET date_in = :in, date_out = :out, status = :stats
                 WHERE track_num_in = :track_num""",
                 {'track_num': num_updated,'in': date_in_updated,'out': date_out_updated,'stats': status_updated})

    conn.commit()
    conn.close()

def delete_one():
    conn = sqlite3.connect("tracking.db")
    c = conn.cursor()

    deleted = input("Enter item to be deleted (track in): ")
    j = convert(deleted)

    c.execute("DELETE from infos WHERE track_num_in = ?", j)
    print("Item deleted successfully")

    conn.commit()
    conn.close()


def delete_table():
    conn = sqlite3.connect("tracking.db")
    c = conn.cursor()

    c.execute("DROP TABLE infos")
    print("Table dropped")

    conn.commit()
    conn.close()
