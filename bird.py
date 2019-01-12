import requests
import json
import uuid
import random
import string

class bird_watch:
    def __init__(self):
        self.bird_url = 'https://api.bird.co/user/login'
        self.guid = ''
        self.email = ''
        self.request_body = {
            'email': self.email
        }
        self.request_headers = {
            'Content-Type': 'application/json',
            'Device-id': self.guid,
            'Platform': 'ios'
        }
        self.bird_response_raw = ''
        self.token = ''
        self.longitude = ''
        self.latitude = ''

    def update_login_info(self):
        self.guid = str(uuid.uuid4())
        self.email = ''.join(random.choice(string.ascii_uppercase+string.digits+string.ascii_lowercase) for i in range(6)) + '@gmail.com'
        self.request_body['email'] = self.email
        self.request_headers['Device-id'] = self.guid

    def login(self):
        # self.update_login_info()
        self.token = None
        attempt = 0
        while self.token is None and attempt < 10:
            try:
                bird_response_raw = requests.post(url=self.bird_url, json=self.request_body, headers=self.request_headers)
                self.token = bird_response_raw.json()['token']
            except:
                attempt += 1
                print("attempt ", attempt)
        if attempt < 10:
            print("Login successful")
        else:
            print("Login unsuccessful")

    def request(self):
        pass

'''
Next steps:
2. get request birds in IV
3. append data into file
'''
