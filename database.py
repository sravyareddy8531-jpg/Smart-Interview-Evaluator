import sqlite3


def create_database():
    connection = sqlite3.connect("interview.db")
    cursor = connection.cursor()

    # Candidates table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    # Results table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            score INTEGER NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_candidate(name, email):
    connection = sqlite3.connect("interview.db")
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO candidates (name, email) VALUES (?, ?)",
        (name, email)
    )

    connection.commit()
    connection.close()


def get_candidates():
    connection = sqlite3.connect("interview.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM candidates")
    candidates = cursor.fetchall()

    connection.close()

    return candidates


def save_result(name, email, score):
    connection = sqlite3.connect("interview.db")
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO results (name, email, score) VALUES (?, ?, ?)",
        (name, email, score)
    )

    connection.commit()
    connection.close()

def get_results():
    connection = sqlite3.connect("interview.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM results")
    results = cursor.fetchall()

    connection.close()

    return results



create_database()