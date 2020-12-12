import re

class Regex_patterns:
    def url(self):
        return "(http(s)?://)?(www.)?[a-z0-9-]+.[a-z]+([a-z0-9/.:=?_&#]+)?"
    
    def domain(self):
        return "(http(s)?://)?(www.)?[a-z0-9-]+.[a-z]+"

    def email(self):
        return "[a-zA-Z0-9.\-_]+@[0-9a-zA-Z]+[0-9a-zA-Z.\-]+"
    
    def phone_number(self):
        return "[+(\d]{1}[\d+() ]{4,12}[\d]{1}"

    def comment(self):
        return "<!--[ -~]*-->"