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

        self.domain = re.search(Regex_patterns().domain(), self.url).group()
        self.date = date.today().strftime("%d.%m.%Y")
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
        print("crawled_links")
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
            web_content = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
        except:
            web_content = ""

        return web_content
    
    def find_links(self, web_content):
        link = ""

        for i in web_content.find_all("a", href=True):
            if re.match(Regex_patterns().url(), i["href"]):
                link = i["href"]
            elif i["href"].startswith("/"):
                link = self.domain + i["href"]

            if link != "" and link not in self.links:
                self.links.append(link)

    def find_emails(self, web_content):
        emails = re.findall(Regex_patterns().email(), web_content)
        for i in range(len(emails)):
            if emails[i] not in self.emails:
                self.emails.append(emails[i])

    def find_phone_numbers(self, web_content):
        phone_numbers = re.findall(Regex_patterns().phone_number(), web_content)
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
                    web_content = self.download_site(self.links[i])

                    if web_content != "":
                        # Find links for sub-sites
                        self.find_links(web_content)
                        
                        # Find emails
                        self.find_emails(web_content.get_text())
                        
                        # Find phone numbers
                        self.find_phone_numbers(web_content.get_text())
                        
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