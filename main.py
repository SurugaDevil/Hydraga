# This is the program that we are currently testing
# Current goal- find most recent update on a Github repository
print("Welcome to Hydraga! Type 'help' for a list of commands.\n")

# importing necessary libraries
from bs4 import BeautifulSoup
import requests
import re

url = input('Enter your URL here: ')

try:
    url = url.strip()
except:
    pass


# cleaning input
if url.startswith("http") == 'True':
    r = requests.get(url)
elif url.startswith("https") == "True":
    r = requests.get(url)
else:
    r = requests.get('http://' +url)

# using Beautiful Soup to obtain source of page
data = r.text
soup = BeautifulSoup(data)
result = (soup.prettify())

# using regex to scrape datetime from result
p = re.compile(r'datetime=\"(.*?)T(.*?)Z\"')
t = re.search(p, result)
result = t.group(1)
result2 = t.group(2)

# print result
print("The last time this repository was edited was: %s %s" % (result, result2))
