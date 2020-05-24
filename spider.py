#!/usr/bin/env python

import requests
import re
import urlparse

def request(url, protocol):
    try:
        #print(protocol+url)
        return requests.get(protocol+url)
    except Exception:
        pass

def extract_web_links(target_url, protocol):
    response = request(target_url, protocol)
    print("[+] web target ==> " + protocol + target_url)
    print(response)
    if response:
        return re.findall('(?:href=")(.*?)"', response.content)
    else:
        return []

def crawling_internal(target_url, protocol, list_discover_links):
    href_links = extract_web_links(target_url, protocol)
    for link in href_links:
        link = urlparse.urljoin(protocol+target_url,link)
        if "#" in link:
            link = link.split("#")[0]+link.split("#")[1]
        if target_url in link and link not in list_discover_links:
            list_discover_links.append(link)
            #print("\t [+] reference link ==> "+link)
            list_discover_links=crawling_internal(link.replace("https://", "").replace("http://",""), protocol, list_discover_links)
    return list_discover_links

target_url ="youtwebsite"
protocol ="https://"
list_discover_links=[]

list_discover_links = crawling_internal(target_url, protocol,list_discover_links)
print("[+] Target url = "+protocol+target_url)
for link  in list_discover_links:
    print("\t[+] discovered link ==> "+link)
