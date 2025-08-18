import os
from dataclasses import dataclass
import sqlite3
from sqlite3 import Connection

@dataclass
class Database:
    """ DB Manager"""
    filename: str
    connection: Connection = None
    
    def __post_init__(self) -> None:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(script_dir, self.filename)
        self.connection = sqlite3.connect(db_path)
        
        self.run(query="""
        CREATE TABLE IF NOT EXISTS Expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            category TEXT,
            comment TEXT,
            date TEXT
        )
        """)

    def run(self, *, query: str, params: tuple = (), fetch: bool = False):
        """Query runner

        Args:
            query (str): Query itself
            fetch (bool, optional): .fetchall() method flag. Defaults to False.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            
            if fetch:
                return cursor.fetchall()

        except sqlite3.Error as e:
            print("DB Error: {}\nQuery: {}".format(e, query))
            raise


