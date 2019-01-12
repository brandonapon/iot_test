import requests
import json
import uuid

bird_url = 'https://api.bird.co/user/login'
guid = str(uuid.uuid4())
request_body = {
    'email': 'iot_test@gmail.com'
}

request_headers = {
    'Content-Type': 'application/json',
    'Device-id': guid,
    'Platform': 'ios'
}

#Printing input
print("bird_url = ")
print(bird_url)

print("request_body = ")
print(request_body)

print("request_headers = ")
print(request_headers)

#Sending POST request
bird_response = requests.post(url=bird_url, json=request_body, headers=request_headers)

#Printing response
print(bird_response)
print(bird_response.json())
