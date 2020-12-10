from regex_patterns import Regex_patterns
import re
import time

class Crawley:
    def welcome(self):
        print("Initializing...")
        for i in range (3, 0, -1):
            time.sleep(0.3)
            print(str(i) + "...")
        print("Hello friend, I'm Crawley - Your personal web crawling assistant.")

    def crawl_another(self):
        pass
    
    def goodbye(self):
        pass

    def user_input(self):
        regex = Regex_patterns()

        # Check what URL the user would like to crawl
        while True: 
            url = input("Please specify what URL you would like to crawl: ").lower()
            if re.match(regex.url, url):
                break
            else:
                print("Oops! Your formatting is invalid, try again!")
                   
        # Check how many levels the user would like to crawl
        while True:
            levels = input("How many levels would you like to crawl? ")
            try:
                levels = int(levels)
            except:
                print("Oops! You have to type a number without decimals.")
                continue
            if levels > 0 and levels <= 100:
                break
            else:
                print("Oops! You have to type a number between 1 and 100.")

        # Check if the user would like to define a regex
        define_regex = self.yes_no_question("So, would you like to define a regex to find special data? y/n: ")
        user_defined_regex = []
        
        # Check what the user-defined regex is, and if the user wants to define more than one.
        if define_regex == True:
            user_defined_regex.append(self.add_regex())
            while True:
                print("Thanks, friend!")
                additional_regex = self.yes_no_question("Would you like to add an additional regex? y/n: ")
                if additional_regex == True:
                    user_defined_regex.append(self.add_regex())
                else:
                    break
        
        #return variables
        return url, levels, user_defined_regex

    def yes_no_question(self, question: str) -> bool:
        while True:
            answer = input(question).lower()
            if answer == "y":
                value = True
                break
            elif answer == "n":
                value = False
                break
            else:
                print("Oops! You need to type either \"y\" for yes or \"n\" for no.")
        return value

    def add_regex(self) -> str:
        regex = str(input("What regex would you like to use? You don't have to encapsualte it in \"\", I'll take care of that for you! "))
        return regex
