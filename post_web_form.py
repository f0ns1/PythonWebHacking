#!/usr/bin/env python

import requests

url = ""
data ={"username": "", "password": "", "Login":"submit" }
response = requests.post(url, data=data)
print(response.content)