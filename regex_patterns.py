import re

class Regex_patterns:
    def __init__(self):
        self.url = "(http(s)?://)?(www.)?[a-z0-9-]+.[a-z]+([a-z0-9/.:=?_&#]+)?"
        self.domain = "(http(s)?://)?(www.)?[a-z0-9-]+.[a-z]+"
        self.email = "[a-zA-Z0-9.\-_]+@[0-9a-zA-Z]+[0-9a-zA-Z.\-]+"
        self.phone_number = ""