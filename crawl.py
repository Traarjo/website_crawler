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
        self.links_to_crawl = [self.url]
        self.crawled_links = []
        self.emails = []
        self.phone_numbers = []
        self.comments = []
        self.special_data = []
        self.common_words = {}

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
        print(self.links_to_crawl)
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

            if link != "" and link not in self.links_to_crawl:
                self.links_to_crawl.append(link)

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

    def find_comments(self, link, web_content):
        file = open("temporary_file.txt", "w")
        file.write(str(web_content))
        file.close()

        with open("temporary_file.txt") as file:
            for num, line in enumerate(file, 1):
                if re.search(Regex_patterns().html_comment(), line):
                    self.comments.append([link, num, re.search(Regex_patterns().html_comment(), line).group()])
                
                if re.search(Regex_patterns().js_comment(), line):
                    self.comments.append([link, num, re.search(Regex_patterns().js_comment(), line).group()])

        file.close()

    def find_special_data(self, link, web_content):
        for regex in self.user_defined_regex:
            special_data = re.findall(regex, web_content)
            self.special_data.append([link, regex, set(special_data)])

    def find_most_common_words(self, web_content):
        # cleaned_text = ""
        # for char in web_content:
        #     cleaned_text += re.sub(Regex_patterns().word(), "", char)
            

        # words = cleaned_text.split()
        # for word in words:
        #     if word in self.common_words:
        #         self.common_words[word] += 1
        #     else:
        #         self.common_words.update({word: 1}) 
        pass     

    def save_report(self):
        path = f"./reports/{re.search(Regex_patterns().pure_domain(), self.domain).group()}_{self.date}.txt"
        file = open(path, "w")
        text = ""

        text += "URL: " + self.url + "\n"
        text += "Date: " + self.date + "\n"
        text += "Crawled levels: " + str(self.levels) + "\n"

        regexes = ""
        if self.user_defined_regex != []:
            for regex in self.user_defined_regex:
                regexes += (regex + ", ")
            text += "User-defined regexes: " + regexes + "\n"
        else:
            text += "Oops! No user-defined regexes." + "\n"
        
        text += "\n"
        if self.crawled_links != []:
            text += "Crawled links:" + "\n"
            for link in self.crawled_links:
                text += link + "\n"
        else:
            text += "Oops! No crawled links." + "\n"

        text += "\n"
        if self.emails != []:
            text += "Emails:" + "\n"
            for email in self.emails:
                text += email + "\n"
        else:
            text += "Oops! No emails found." + "\n"

        text += "\n"
        if self.phone_numbers != []:
            text += "Phone numbers:" + "\n"
            for phone_number in self.phone_numbers:
                text += phone_number + "\n"
        else:
            text += "Oops! No phone numbers found." + "\n"

        text += "\n"
        if self.comments != []:
            text += "Comments:" + "\n"
            for comment in self.comments:
                text += comment[0] + " on line " + str(comment[1]) + ":" + "\n"
                text += comment[2] + "\n"
                text += "\n"
        else:
            text += "Oops! No comments found." + "\n"


        text += "\n"
        if self.special_data != []:
            text += "Special data:" + "\n"
            for special_data in self.special_data:
                text += "\n"
                text += special_data[0] + " with regex \"" + special_data[1] + "\":" + "\n"
                if special_data[2] != set():
                    for data in special_data[2]:
                        text += data + "\n"
                else: text += "Oops! No special data found." + "\n"
        else:
            text += "Oops! No special data found." + "\n"

        text += "\n"
        # common words

        file.write(text)
        file.close()

    def perform_crawl(self):
        if self.count <= self.levels:      
            for i in range(len(self.links_to_crawl)):
                if self.links_to_crawl[i] not in self.crawled_links:
                    # Download site and get content
                    web_content = self.download_site(self.links_to_crawl[i])

                    if web_content != "":
                        # Find links for sub-sites
                        self.find_links(web_content)
                        
                        # Find emails
                        self.find_emails(web_content.get_text())
                        
                        # Find phone numbers
                        self.find_phone_numbers(web_content.get_text())
                        
                        # Find comments from the source code
                        self.find_comments(self.links_to_crawl[i], web_content)

                        # Find special data
                        self.find_special_data(self.links_to_crawl[i], web_content.get_text())
                        
                        # Find common words
                        self.find_most_common_words(web_content.get_text())

                        # Add link to crawled links
                        self.crawled_links.append(self.links_to_crawl[i])
                    else:
                        print("Oops! " + self.links_to_crawl[i] + " can't be crawled.")
                        continue

            #for i in range(len(self.li))            
            self.increase_count() #TODO: må sjekke om denne hopper før alle linker er sjekket
            self.perform_crawl()