#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import urlparse

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
        post_data={}
        for form in forms_list:
            action = form.get("action")
            post_url = urlparse.urljoin(target_url,action)
            print("\t[+] post url ==> "+post_url)
            print("\t[+] action ==> "+action)
            method = form.get("method")
            print("\t[+] method type ==> "+method)
            input_list= form.findAll("input")
            for input in input_list:
                input_name = input.get("name")
                input_type = input.get("type")
                input_value= input.get("value")
                print("\t\t [+] form input input_name ==> " + str(input_name))
                print("\t\t [+] form input  input_type ==> " + str(input_type))
                print("\t\t [+] form input input_value ==> " + str(input_value))
                post_data[input_name] = input_value
            result= requests.post(post_url,data=post_data)
            print(result)
except Exception as e:
    print(e)
    pass