import sys
from urllib import response
import requests
from privacy import flomo_api

content = ' '.join(sys.argv[1:])

if not content:
    print("Please enter some text to send to Flomo")
    exit(1)

url = flomo_api

header = {'Content-Type': 'application/json'}
body = {'content': content}

response = requests.post(url, headers=header, json=body)

if response.status_code == 200:
    print("Successfully Post to Flomo")
else:
    print("Failed to Post to Flomo")

# input("Press Enter to exit...")
