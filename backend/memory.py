# memory.py

import sqlite3
import os

from config import DATABASE_PATH


os.makedirs("data", exist_ok=True)


class Memory:

    def __init__(self):

        self.conn = sqlite3.connect(DATABASE_PATH)

        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS history(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            command TEXT,
            result TEXT
        )
        """)

        self.conn.commit()

    def save(self, command, result):

        self.cursor.execute(
            """
            INSERT INTO history(command, result)
            VALUES (?, ?)
            """,
            (command, result)
        )

        self.conn.commit()

    def recent(self, limit=10):

        self.cursor.execute(
            """
            SELECT command, result
            FROM history
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,)
        )

        return self.cursor.fetchall()