import sqlite3


def create_database():
    conn = sqlite3.connect('pointing_system.db')
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS pointing_system(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, points INTEGER)")
    conn.commit()
    conn.close()


def add_player(name, points=0):
    conn = sqlite3.connect('pointing_system.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pointing_system (name, points) VALUES (?, ?)", (name, points))
    player_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return player_id


def clear_table():
    conn = sqlite3.connect('pointing_system.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pointing_system")
    conn.commit()
    conn.close()

# Always execute
create_database()

clear_table()
