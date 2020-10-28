import re

def user_input():
    # Check if the user would like to crawl the IMDb Top 1000
    imdb = yes_no_question("Would you like to crawl the IMDb Top 1000? y/n: ")

    # Check what URL the user would like to crawl
    if imdb == True:
        url = "https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating"
    else:
        while True: 
            url = input("What URL would you like to crawl instad? ").lower()
            if re.match("http(s)?://www.[a-z0-9-]+.[a-z]+([a-z0-9/.:=?_&#]+)?", url):
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
    
    # Check what the user-defined regex is
    if define_regex == True:
        while True:
            regex = input("What regex would you like to use? ")
            if regex[0] != "\"" or regex[len(regex) - 1] != "\"" or len(regex) < 3:
                print("Please encapsulate your regex in \"\".")
                continue
            break
    else:
        regex = ""
    
    #return variables
    return url, levels, regex

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
