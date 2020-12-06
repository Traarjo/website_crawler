from regex_patterns import Regex_patterns
from bs4 import BeautifulSoup
import urllib.request
import re

class Crawl:

    def __init__(self, url : str, levels : int, user_defined_regex : list):
        self.url = url
        self.domain = Regex_patterns().domain
        self.levels = levels
        self.user_defined_regex = user_defined_regex
        self.count = 0

    def increase_count(self):
        self.count += 1

    def download_site(self, url):

        print("her")
    
    def perform_jump(self):
        pass

    def perform_crawl(self):
        self.download_site(self.url)