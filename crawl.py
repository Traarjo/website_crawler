from regex_patterns import Regex_patterns
from bs4 import BeautifulSoup
from datetime import date
import urllib.request
import re
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

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

    def find_special_data(self, web_content):
        # data = []

        # for i in range(len(self.user_defined_regex)):
        #     special_data = re.findall(self.user_defined_regex[i], web_content)
        #     for j in range(len(special_data)):
        #         data.append(special_data[j])
        #     self.special_data.append([self.user_defined_regex[i], data])
        pass

    def find_most_common_words(self):
        pass

    def save_to_pdf(self):
        path = f"./reports/{re.search(Regex_patterns().pure_domain(), self.domain).group()}_{self.date}.pdf"
        pdf = canvas.Canvas(path, pagesize=A4)
        text = pdf.beginText()

        width, height = A4
        text.setTextOrigin(50, height - 50)

        text.textLine("URL: " + self.url)
        text.textLine("Date: " + self.date)
        text.textLine("Crawled levels: " + str(self.levels))

        regexes = ""
        if self.user_defined_regex != []:
            for regex in self.user_defined_regex:
                regexes += (regex + ", ")
            text.textLine("User-defined regexes: " + regexes)
        else:
            text.textLine("No user-defined regexes.")
        
        text.textLine("")
        if self.crawled_links != []:
            text.textLine("Crawled links:")
            for link in self.crawled_links:
                text.textLine(link)
        else:
            text.textLine("No crawled links.")

        text.textLine("")
        if self.emails != []:
            text.textLine("Emails:")
            for email in self.emails:
                text.textLine(email)
        else:
            text.textLine("No emails found.")

        text.textLine("")
        if self.phone_numbers != []:
            text.textLine("Phone numbers:")
            for phone_number in self.phone_numbers:
                text.textLine(phone_number)
        else:
            text.textLine("No phone numbers found.")

        text.textLine("")
        if self.comments != []:
            text.textLine("Comments:")
            for comment in self.comments:
                text.textLine(comment[0] + " on line " + str(comment[1]) + ":")
                text.textLine(comment[2])
                text.textLine("")
        else:
            text.textLine("No comments found.")


        text.textLine("")
        # special data

        text.textLine("")
        # common words

        pdf.drawText(text)
        pdf.setTitle("Web Crawl Report")
        pdf.save()


    def perform_crawl(self):
        if self.count <= self.levels:      
            for i in range(len(self.links_to_crawl)):
                if self.links_to_crawl[i] not in self.crawled_links:
                    # Download site and get content
                    web_content = self.download_site(self.links_to_crawl[i])

                    if web_content != "":
                        # Find links for sub-sites
                        #self.find_links(web_content)
                        
                        # Find emails
                        #self.find_emails(web_content.get_text())
                        
                        # Find phone numbers
                        #self.find_phone_numbers(web_content.get_text())
                        
                        # Find comments from the source code
                        #self.find_comments(self.links_to_crawl[i], web_content)

                        # Find special data
                        #self.find_special_data(web_content.get_text())
                        
                        # Find common words

                        # Add link to crawled links
                        self.crawled_links.append(self.links_to_crawl[i])
                    else:
                        print("Oops! That website can't be crawled.")
                        return

            #for i in range(len(self.li))            
            self.increase_count() #TODO: må sjekke om denne hopper før alle linker er sjekket
            self.perform_crawl()