#!/usr/bin/env python

import requests


def request(url, protocol):
    try:
        return requests.get(protocol+url, timeout=1)
    except Exception:
        pass

def check_directories(url, protocol):
    with open("medium.txt", "r") as wordlist_file:
        for line in wordlist_file:
            test_url = url+"/"+line.strip()
            status = request(test_url, protocol)
            if status:
                print("\t\t [+] Discovered new directory ==> " + protocol + test_url)


def check_subdomains(url, protocol):
    with open("Subdomain.txt", "r") as wordlist_file:
        for line in wordlist_file:
            test_url = line.strip() + "." + url
            print("[--] Test =" + test_url)
            status = request(test_url, protocol)
            if status:
                print("\t [+] Discovered subdomain ==> " + protocol + test_url)
                check_directories(test_url, protocol)




url="linkedin.com"
protocol="https://"
check_subdomains(url, protocol)
