#!/usr/bin/env python

import requests

url = ""
data ={"username": "", "password": "", "Login":"submit" }
response = requests.post(url, data=data, allow_redirects=True)
print(response.content)