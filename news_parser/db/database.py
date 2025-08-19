from peewee import SqliteDatabase, IntegrityError
from .article import Article

class Database:
    def __init__(self, path: str) -> None:
        self.db = SqliteDatabase(
            path,
            pragmas={'journal_mode': 'wal'}
        )
        self.db.connect()
        self.db.bind([Article])
        self.db.create_tables([Article])
    
    def add(
        self,
        title: str,
        url: str,
        author: str = None,
        date = None,
        source = None,
        rank = None,
    ):
        try:
            article = Article.create(
                title=title,
                url=url,
                author=author,
                date=date,
                source=source,
                rank=rank,
            )
            
            return article
        
        except IntegrityError:
            print(f'[DB] Article with URL {url} already exists')
            return None
        else:
            print(f"Article {article} successfuly added")