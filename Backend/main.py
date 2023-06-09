import random
import re

class Bot:

    def __init__(self):
        # Class main var
        self.start = input("Type Here: ")
        self.beginning_loop = True
        self.opening = []
        self.meeting = []
        self.main = []
        self.credit_score = []
        self.end = False

        # Start/Stop var
        self.greetings = ["Hi", 'Hello', 'Hey there!']
        self.exit = ["Bye", "Goodbye", "See Ya", "Quit", "Exit", "End", "Stop"]
        self.exit_reponses = ["Come back if you have more questions!", "Have a great day!"]

        # Credit var and dict
        self.precr = True
        self.credit_bureaus = ["Experian", "Transunion", "Equifax"]
        self.credit = {
            "Excellent credit! I have stored your credit score for later. ": list(range(750,851)),
            "Good credit! I have stored your credit score for later. ": list(range(700, 750)),
            "Average credit. I have stored your credit score for later. ": list(range(620, 700)),
            "Below Average credit. I have stored your credit score for later. ": list(range(600, 620)),
            "Bad credit. I have stored your credit score for later. ": list(range(300, 600))
        }

        #     string_func = {credit : '*credit*'

        #                    }
        # Investing var
        self.index_funds = ['SPY', 'NASDAQ', 'Dow Jones', 'Gold Select']

    def greeting(self):
        self.opening = input("Hello, I am your personal finance chatbot! What's your name? ")

    def quit(self):
        print(random.choice(self.exit_reponses))
        self.end = True

    def invest(self):
        print(random.choice(self.index_funds))

# We will run the input score against the iteration of the credit key, value dictionary, if we find the value we return the key

    def creditRating(self):
        self.credit_score = input("What is your credit score? ")
        for key, value in self.credit.items():
            if int(self.credit_score) in value:
                print(key)
                self.precr = False
                self.beginning = False
                return self.mainLoop()
            
            elif self.credit_score < str(300) or self.credit_score > str(850):
                print("Error: Out of FICO range ")
                return self.mainLoop()

# Intitalizing loop where we learn about the user and store data to be used at a later date
# In each case we check if the input ever equals any exit queues which will break the loop and terminate the bot entirely

    def startLoop(self):
        while self.beginning_loop == True:

            if self.start in self.exit:
                self.quit()
                break

            if self.start in self.greetings:
                self.greeting()
                func = True

            elif self.start not in self.greetings:
                func = False
                x = True

                if x == True:
                    self.main = input(random.choice(self.greetings))
                    x = False

                elif x == False:
                    if self.main not in self.exit:
                        self.beginning = False
                        return self.mainLoop()

            if self.opening in self.exit:
                self.quit()
                break
                
            if func == True:
                func == False
                self.meeting = input(f"Nice to meet you {self.opening}! What part of finance or investing are you interested in? ")
                     
            if "credit" in self.meeting:
                self.creditRating()
                
            elif self.meeting not in self.opening:
                if self.meeting in self.exit:
                    self.quit()
                    break
                else:
                    self.beginning = False
                    self.mainLoop()

# After the inital loop is ran through, it will be directed to this mainLoop method which will be present for the rest of the chat log

    def mainLoop(self):
        if self.beginning == False:
            while self.main not in self.exit:
                if "credit" in self.main and self.precr == True:
                    self.creditRating()
                else:
                    self.main = input("What would you like to talk about? ")


bot = Bot()
bot.startLoop()
