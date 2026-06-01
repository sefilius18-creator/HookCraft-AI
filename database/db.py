import sqlite3

conn = sqlite3.connect(
    "hookcraft.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    feature TEXT,
    prompt TEXT,
    result TEXT
)
""")

conn.commit()


def save_history(feature, prompt, result):

    cursor.execute(
        """
        INSERT INTO history
        (feature,prompt,result)
        VALUES (?,?,?)
        """,
        (feature,prompt,result)
    )

    conn.commit()


def get_history():

    cursor.execute(
        """
        SELECT * FROM history
        ORDER BY id DESC
        """
    )

    return cursor.fetchall()
