import sys
import requests

# Get the content sent to the server from the command line
content = ' '.join(sys.argv[1:])

# get url settings
try:
    # if there is already a url in the content, use it
    with open('url.txt', 'r') as f:
        url = f.read()
except FileNotFoundError:
    # if there is no url in the content, ask the user for one (for the first time)
    with open('url.txt', 'w') as f:
        url = input('Enter your Flomo API URL: ')
        f.write(url)

# if there is no content, terminate the program
if not content:
    print("Please enter some text to send to Flomo")
    exit(1)
    

# set the headers and payload for the request
header = {'Content-Type': 'application/json'}
body = {'content': content}

# send the request and get the response
response = requests.post(url, headers=header, json=body)

# print the response, which will not be shown in listary
if response.status_code == 200:
    print("Successfully Post to Flomo")
else:
    print("Failed to Post to Flomo")

# input("Press Enter to exit...")
