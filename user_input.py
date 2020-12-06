from regex_patterns import Regex_patterns
import re

def user_input():
    regex = Regex_patterns()

    # Check what URL the user would like to crawl
    while True: 
        url = input("What URL would you like to crawl? ").lower()
        if re.match(regex.url, url):
            break
        else:
            print("Invalid format, try again.")
            print("Tips: URL must start with \"https://\" or \"http://\" and \"www.\" must be included.")
                
    # Check how many levels the user would like to crawl
    while True:
        levels = input("How many levels would you like to crawl? ")
        try:
            levels = int(levels)
        except:
            print("You have to type a number without decimals.")
            continue
        if levels > 0 and levels <= 100:
            break
        else:
            print("You have to type a number between 1 and 100.")

    # Check if the user would like to define a regex
    define_regex = yes_no_question("Would you like to define a regex to find sensitive data? y/n: ")
    user_defined_regex = []
    
    # Check what the user-defined regex is, and if the user wants to define more than one.
    if define_regex == True:
        user_defined_regex.append(add_regex())
        while True:
            additional_regex = yes_no_question("Would you like to add an additional regex? y/n: ")
            if additional_regex == True:
                user_defined_regex.append(add_regex())
            else:
                break
    
    #return variables
    return url, levels, user_defined_regex

def yes_no_question(question: str) -> bool:
    while True:
        answer = input(question).lower()
        if answer == "y":
            value = True
            break
        elif answer == "n":
            value = False
            break
        else:
            print("You need to type either \"y\" for yes or \"n\" for no.")
    return value

def add_regex() -> str:
    regex = str(input("What regex would you like to use? No surrounding \"\" needed. "))
    return regex
