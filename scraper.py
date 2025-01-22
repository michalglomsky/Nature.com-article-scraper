import requests
import string
from bs4 import BeautifulSoup
from http import HTTPStatus

"""# Taking the URL from the input
input_url = input('Input the URL:\n> ')"""

input_url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3"

# Getting the response message form the page
page = requests.get(input_url)

# Checking for error in the status code
if page.status_code != HTTPStatus.OK:
    # printing the error message
    print("The URL returned " + str(page.status_code) + "!")
    exit()

# Creating soup for our page
soup = BeautifulSoup(page.content, 'html.parser')
# Finding all <article> tags
articles_soup = soup.find_all('article')

# Initializing an empty dictionary of articles
articles = []

# Loop for finding right articles and extracting information about them
for a in articles_soup:
    # Looking for article type "News" inside <span> tag
    article_type = a.find('span', {'data-test': 'article.type'})
    if article_type.text == "News":

        "Finding the headline, opening the file and formatting it's name"
        # Finding the headline in <h3> tag
        headline = a.find('h3', {'itemprop': 'name headline'}).text
        # Sanitize the headline for file naming
        headline = headline.strip()  # Remove leading and trailing whitespace, including \n
        # Removing punctuation and whitespaces between words
        for char in headline:
            if char in string.punctuation:
                headline = headline.replace(char, '')
            if char == " ":
                headline = headline.replace(char, '_')
        # Adding file format
        headline += '.txt'

        # Opening the file and naming it
        file = open(headline, "w", encoding="utf-8")
        # Keeping track of the article names in the 'articles' array
        articles.append(headline)

        "Finding the article body and writing it into the file"
        # Finding proper <a> tag to access the article body
        article_hyperlink = a.find('a', {'data-track-action' : 'view article'})
        # Entering the hyperlink to extract the content from the article body
        link = "https://www.nature.com/nature" + article_hyperlink['href']
        # Sending a request to the link
        article_body = requests.get(link)
        # Creating soup to extract the content of the article
        soup_body = BeautifulSoup(article_body.content, 'html.parser')
        # Extracting the content
        content = soup_body.find('p', {"class": "article__teaser"}).text
        # Writing the content into the file
        file.write(content)
        file.close()

print(articles)