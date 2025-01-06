import requests

# Taking the URL from the input
url = input('Input the URL:\n> ')

# Setting headers to accept JSON format
headers = {'Accept': 'application/json'}

# Creating a response object from the URL
response = requests.get(url, headers=headers) # Added the headers

json_data = response.json()
# Creating a conditional output
if json_data['status']<300:
    # Parse the JSON response
    print(json_data['joke'])
else:
    # Printing the error message
    print('Invalid resource!')