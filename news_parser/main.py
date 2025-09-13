from datetime import datetime
from parser import Parser
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from db.database import Database
from utils import maybe

URL = "https://news.ycombinator.com/"

db = Database("parsed.db")
parser = Parser()


def recursive_parser(url: str, parser: Parser):
    soup = parser.fetch(url).make_soup()
    more_link = soup.find("a", {"class": "morelink"})

    if not more_link:
        return None

    process_data(soup)

    return recursive_parser(url=urljoin(URL, more_link.get("href")), parser=parser)


def process_data(data: BeautifulSoup) -> None:
    rows = data.find_all("tr", {"class": "athing"})

    for row in rows:
        next_row = row.find_next_sibling()

        title_tag = row.find("span", {"class": "titleline"}).find("a")
        author_tag = next_row.find("a", {"class": "hnuser"})
        rank_tag = next_row.find("span", {"class": "score"})
        source_tag = row.find("span", {"class": "sitestr"})
        date_tag = next_row.find("span", {"class": "age"})

        db.add(
            title=maybe(title_tag, lambda x: x.text.strip()),
            url=maybe(title_tag, lambda x: x.get("href")),
            author=maybe(author_tag, lambda x: x.text.strip()),
            date=maybe(
                date_tag, lambda x: datetime.fromisoformat(x.get("title").split()[0])
            ),
            source=maybe(source_tag, lambda x: x.text.strip()),
            rank=maybe(rank_tag, lambda x: float(x.text.split()[0])),
        )


recursive_parser(url=URL, parser=parser)
print(f"Total articles: {db.count()}")
