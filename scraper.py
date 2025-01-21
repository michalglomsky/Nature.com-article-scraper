import requests
from http import HTTPStatus

# Taking the URL from the input
input_url = input('Input the URL:\n> ')

# Opening the file for saving content of the page from the URL
# Setting mode to writing in bytes
source = open('source.html', 'wb')

# Getting the response message form the page
page = requests.get(input_url)

# Checking for error in the status code
if page.status_code != HTTPStatus.OK:
    # printing the error message
    print("The URL returned " + str(page.status_code) + "!")
    exit()

# Writing the content of the page into the source.html
source.write(page.content)

# Printing a success message
print("Content saved.")