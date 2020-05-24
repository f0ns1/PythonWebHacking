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

target_url="http://10.0.9.6/mutillidae/index.php?page=dns-lookup.php"
response = request(target_url)
try:
    if response.content:
        parsed_html = BeautifulSoup(response.content)
        forms_list = parsed_html.findAll("form")
        for form in forms_list:
            action = form.get("action")
            print("\t[+] action ==> "+action)
            method = form.get("method")
            print("\t[+] method type ==> "+method)
            input_list= form.findAll("input")
            for input in input_list:
                print("\t\t [+] form inputs ==> "+input)

except Exception as e:
    print(e)
    pass