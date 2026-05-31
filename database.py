import sqlite3
from datetime import date

DB_NAME = "hookcraft.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic TEXT,
        style TEXT,
        result TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS usage (
        usage_date TEXT PRIMARY KEY,
        count INTEGER
    )
    """)

    conn.commit()
    conn.close()

def get_daily_usage():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    today = str(date.today())

    cur.execute(
        "SELECT count FROM usage WHERE usage_date=?",
        (today,)
    )

    row = cur.fetchone()

    conn.close()

    return row[0] if row else 0

def increase_usage():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    today = str(date.today())

    cur.execute("""
    INSERT INTO usage(usage_date,count)
    VALUES(?,1)
    ON CONFLICT(usage_date)
    DO UPDATE SET count=count+1
    """,(today,))

    conn.commit()
    conn.close()

def save_history(topic, style, result):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO history(topic,style,result)
    VALUES(?,?,?)
    """,(topic,style,result))

    conn.commit()
    conn.close()

def get_history():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    SELECT topic,style,result,created_at
    FROM history
    ORDER BY id DESC
    LIMIT 20
    """)

    rows = cur.fetchall()

    conn.close()

    return rows
