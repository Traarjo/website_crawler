from regex_patterns import Regex_patterns
from bs4 import BeautifulSoup
from datetime import date
import urllib.request
import re

class Crawl:
    def __init__(self, url : str, levels : int, user_defined_regex : list):
        self.url = url
        self.levels = levels
        self.user_defined_regex = user_defined_regex

        self.domain = re.search(Regex_patterns().domain, self.url).group()
        self.date = date.today().strftime('%d.%m.%Y')
        self.count = 1
        self.links = [self.url]
        self.crawled_links = []
        self.website_content = ""

    def increase_count(self):
        self.count += 1

    def download_site(self, url):
        content = str(urllib.request.urlopen(url).read())
        self.website_content = content
    
    def find_links(self):
        pass
    #href
    #src

    def find_emails(self):
        pass

    def find_phone_numbers(self):
        pass

    def find_comments(self):
        pass

    def find_special_data(self):
        pass

    def find_most_common_words(self):
        pass

    def save_to_pdf(self):
        pass

    def save_site(self):
        pass
        # Save site to textfile in domain/date/file

    def perform_crawl(self):
        if self.count <= self.levels:      
            for i in range(len(self.links)):
                if self.links[i] not in self.crawled_links:
                    self.download_site(self.links[i])
                    #download
                    #get links
                    #get email
                    #get phone numbers
                    #get comments
                    #get special data
                    #get common words
                    self.crawled_links.append(self.links[i])

            self.increase_count()
            self.perform_crawl()