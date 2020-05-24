#!/usr/bin/env python

import requests
import re

def request(url, protocol):
    try:
        return requests.get(protocol+url)
    except Exception:
        pass

target_url ="marca.com"
protocol ="https://"
response = request(target_url, protocol)
print("[+] web target ==> "+protocol+target_url)
href_links =re.findall('(?:href=")(.*?)"', response.content)

for link in href_links:
    print("\t [+] reference link ==> "+link)