from peewee import SqliteDatabase

db = SqliteDatabase("database.sqlite3")

class Database:
    def __init__(self, db_instance):
        self.db = db_instance
        
    def __enter__(self):
        self.db.connect(reuse_if_open=True)
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        if not self.db.is_closed():
            self.db.close()
    
    # Optional: transaction helper
    def transaction(self):
        return self.db.atomic()
