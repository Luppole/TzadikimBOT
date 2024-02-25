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


def find_id(name):
    conn = sqlite3.connect('pointing_system.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM pointing_system WHERE name=?", (name,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None


def find_player(player_id):
    conn = sqlite3.connect('pointing_system.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pointing_system WHERE id=?", (player_id,))
    row = cursor.fetchone()
    conn.close()
    return row[1]


def add_points(player_id, points_to_add):
    conn = sqlite3.connect('pointing_system.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE pointing_system SET points = points + ? WHERE id = ?", (points_to_add, player_id))
    conn.commit()
    conn.close()

def get_points(name):
    conn = sqlite3.connect('pointing_system.db')
    cursor = conn.cursor()
    cursor.execute("SELECT points FROM pointing_system WHERE name=?", (name,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None


# Always execute
create_database()