from parser import Parser
from db.database import Database
from datetime import datetime
from utils import maybe

URL = 'https://news.ycombinator.com/'

db = Database('parsed.db')
parser = Parser()

data = parser.fetch(URL).make_soup()

for row in data.find_all('tr', { 'class': 'athing'}):
    next_row = row.find_next_sibling()
    
    title_tag = row.find('span', { 'class': 'titleline' }).find('a')
    author_tag = next_row.find('a', { 'class': 'hnuser' })
    rank_tag = next_row.find('span', { 'class': 'score' })
    source_tag = row.find('span', { 'class': 'sitestr' })
    date_tag = next_row.find('span', { 'class': 'age' })
    
    db.add(
        title=maybe(title_tag, lambda x: x.text.strip()),
        url=maybe(title_tag, lambda x: x.get('href')),
        author=maybe(author_tag, lambda x: x.text.strip()),
        date=maybe(
            date_tag,
            lambda x: datetime.fromisoformat(x.get('title').split()[0])
        ),
        source=maybe(source_tag, lambda x: x.text.strip()),
        rank=maybe(rank_tag, lambda x: float(x.text.split()[0])),
    )
    
