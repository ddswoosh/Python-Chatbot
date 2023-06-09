import requests
from bs4 import BeautifulSoup
import pandas as pd

#Start by scraping forums for conversations which we can later store in a database to train the chatbot

url = "https://ficoforums.myfico.com/t5/Credit-Cards/Best-New-Credit-Cards/m-p/6602156"
response = requests.get(url)

doc = BeautifulSoup(response.text, "html.parser")

formatted = doc.prettify()

string = doc.find_all("p")

#Format replies and responses in a table as a CSV so we can import to a sql database
tags = []
for tag in enumerate(string):
    tags = tag
print(list(tags))
