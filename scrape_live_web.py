#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 13:05:23 2024

@author: spencerharris
"""

from bs4 import BeautifulSoup
import requests

# Provide the web address of the live web
url = 'http://libraries.uky.edu'
# Obtain information from the live web
page = requests.get(url)
# Parse the page to obtain the parent div tag
soup = BeautifulSoup(page.text, "html.parser")
div = soup.find('div', class_="slab global-footer")
# Locate the three child div tags
contacts = div.find_all("div", class_="global-footer__column")
# Print out the first child div tag to examine it
print(contacts[0])

# Obtain information from each child tag
# Below here doesnt work, this was built for a previous simplified version of this page
for contact in contacts:
    # Obtain the area name
    area = contact.find('div', class_="block-contactus")
    print(area.text)
    # Obtain the phone and email
    atags = contact.find_all('a', href = True)
    for atag in atags:
        print(atag.text)