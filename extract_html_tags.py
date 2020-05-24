#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup


def request(url):
    try:
        print(url)
        return requests.get(url, allow_redirects=True)
    except Exception as e:
        print(e)
        pass

target_url="your url ...."
response = request(target_url)
try:
    if response.content:
        parsed_html = BeautifulSoup(response.content)
        forms_list = parsed_html.findAll("form")
        for tag in forms_list:
            print("\t[+] form tag ==> "+str(tag))
except Exception as e:
    print(e)
    pass