import requests
from bs4 import BeautifulSoup

class Parser:
    def __init__(self):
        self.data = None
    
    def fetch(self, url: str):
        try:
            response = requests.get(url)
            response.raise_for_status()
            self.data = response.text
            
            return self
            
        except Exception as e:
            print(f"[Parser Error] | {e}")
            self.data = None
            
            return self

    def make_soup(self) -> BeautifulSoup:
        if not self.data:
            raise ValueError('No data in the parser. Please fetch first!')

        return BeautifulSoup(self.data, 'html.parser')
