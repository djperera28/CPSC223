## Name: David Perera
# Student ID: 884532367
# Section: 07
# Assignment: Module 10 Assignment 3
import requests
from bs4 import BeautifulSoup

hostname = input("What is the hostname? (ex: www.edhrec.com/commanders) ")
response = requests.get("http://" + hostname)
soup = BeautifulSoup(response.text, "html.parser")

print("Here is the HTML:")
print(response.text)

#finding the names of top mtg commanders on the edhrec Website
print("Here are the Top Commander names:")
for link in soup.find_all("a"):
    if link.get("href", "").startswith("/commanders/"):
        name = link.get_text(strip=True)
        if name:
            print(name)
