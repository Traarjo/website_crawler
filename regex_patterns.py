import re

class Regex_patterns:
    def __init__(self):
        self.url = "(http(s)?://)?(www.)?[a-z0-9-]+.[a-z]+([a-z0-9/.:=?_&#]+)?"
        self.domain = "(http(s)?://)?(www.)?[a-z0-9-]+.[a-z]+"