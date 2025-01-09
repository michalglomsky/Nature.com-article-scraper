import requests
from bs4 import BeautifulSoup

# Taking the URL from the input
url = input('Input the URL:\n> ')

# Checking the validity of the page
if "nature.com" not in url or "articles" not in url:
    print("Invalid page!")
    exit()

# Creating a response object from the URL
# Accepting only English pages
r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
# Parsing the page
soup = BeautifulSoup(r.content, 'html.parser')

# Initializing the output array
article = {"title": "", "description": ""}
# Initializing <head>
tag_head = soup.find('head')

# Checking if the article has <head>
if tag_head:
    # Looking for and checking if there is valid <title>
    tag_title = tag_head.find('title')
    if tag_title:
        article["title"] = tag_title.text
    else:
        print("Invalid page!")
        exit()
    # Looking for and checking if there is valid <meta name="description">
    tag_meta_description = tag_head.find('meta', {"name": "description"})
    if tag_meta_description:
        article["description"] = tag_meta_description["content"]
    else:
        print("Invalid page!")
        exit()

# Printing article dictionary with "title" and "description"
print(article)
