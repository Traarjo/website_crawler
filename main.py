from user_input import user_input
from crawl import Crawl
        
url, levels, user_defined_regex = user_input()

crawl = Crawl(url, levels, user_defined_regex)
print(crawl.url)