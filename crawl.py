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
        self.emails = []
        self.phone_numbers = []
        self.comments = []
        self.special_data = []
        self.common_words = []

    def test_variables(self):
        print("url")
        print(self.url)
        print("levels")
        print(self.levels)
        print("user_defined_regex")
        print(self.user_defined_regex)
        print("domain")
        print(self.domain)
        print("date")
        print(self.date)
        print("count")
        print(self.count)
        print("links")
        print(self.links)
        print("crawled_linkjs")
        print(self.crawled_links)
        print("emails")
        print(self.emails)
        print("phone_numbers")
        print(self.phone_numbers)
        print("comments")
        print(self.comments)
        print("special_data")
        print(self.special_data)
        print("common_words")
        print(self.common_words)

    def increase_count(self):
        self.count += 1

    def download_site(self, url):
        try:
            content = str(urllib.request.urlopen(url).read())
        except:
            content = ""

        return content
    
    def find_links(self):
        pass
    #href
    #src

    def find_emails(self, website_content):
        emails = re.findall(Regex_patterns().email, website_content)
        for i in range(len(emails)):
            if emails[i] not in self.emails:
                self.emails.append(emails[i])

    def find_phone_numbers(self, website_content):
        phone_numbers = re.findall(Regex_patterns().phone_number, website_content)
        for i in range(len(phone_numbers)):
            if phone_numbers[i] not in self.phone_numbers:
                self.phone_numbers.append(phone_numbers[i])

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
                    # Download site and get content
                    website_content = self.download_site(self.links[i])

                    if website_content != "":
                        # Find links for sub-sites
                        
                        # Find emails
                        self.find_emails(website_content)
                        
                        # Find phone numbers
                        self.find_phone_numbers(website_content)
                        
                        # Find comments from the source code

                        # Find special data
                        
                        # Find common words

                        # Add link to crawled links
                        self.crawled_links.append(self.links[i])
                    else:
                        print("Oops! That website can't be crawled.")
                        return

            self.increase_count() #TODO: må sjekke om denne hopper før alle linker er sjekket
            self.perform_crawl()