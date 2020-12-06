from bs4 import BeautifulSoup
import urllib.request
import re

class Crawl:
    def __init__(self, url : str, levels : int, user_defined_regex : list):
        self.url = url
        self.levels = levels
        self.user_defined_regex = user_defined_regex

    def download_site(self):
        pass
    
    def jump(self):
        pass

    def perform_crawl(self):
        pass