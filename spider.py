#!/usr/bin/env python

import requests
import re
import urlparse

def request(url, protocol):
    try:
        return requests.get(protocol+url)
    except Exception:
        pass

def extract_web_links(target_url, protocol):
    response = request(target_url, protocol)
    print("[+] web target ==> " + protocol + target_url)
    return re.findall('(?:href=")(.*?)"', response.content)


target_url ="yourweb..."
protocol ="https://"
list_dicover_links = []
href_links = extract_web_links(target_url, protocol)

for link in href_links:
    link = urlparse.urljoin(protocol+target_url,link)
    if "#" in link:
        link = link.split("#")[0]+link.split("#")[1]
    if target_url in link and link not in list_dicover_links:
        list_dicover_links.append(link)
        print("\t [+] reference link ==> "+link)