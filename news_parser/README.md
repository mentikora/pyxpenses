# Project: “Top News Scraper & Search Engine”

### Goal: Build a Python parser that scrapes news headlines from a website, stores them in SQLite, and allows querying/searching.

#### Tools & Libraries:

- Python

- Requests

- BeautifulSoup (bs4)

- SQLite

- Optional: Click or argparse for CLI commands

#### Tasks

Use requests to grab HTML from a news site (e.g., https://news.ycombinator.com/
)

#### Task: Handle potential request errors (timeouts, status codes, etc.)

Use BeautifulSoup to extract:

- Headline text

- URL

- Author (if available)

- Date/Time (if available)

#### Task: Make sure parsing works even if some fields are missing

Store in SQLite

Create a simple table: News(id INTEGER PRIMARY KEY, title TEXT, url TEXT, author TEXT, date TEXT)

#### Task: Insert only unique headlines (avoid duplicates)

Query/search

Implement CLI commands or simple functions:

- List all headlines

- Search by keyword

- Search by author

- Count how many articles are scraped

#### Bonus (optional)

- Schedule the scraper to run daily (using schedule library or cron job)

- Export search results to CSV

- Detect and update changes in headlines (if URLs already exist)
