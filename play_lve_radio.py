#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 18:12:14 2024

@author: spencerharris
"""

# Put your web driver in the same folder as this script
from selenium import webdriver
browser = webdriver.Chrome(executable_path='./chromedriver')
browser.get("https://onlineradiobox.com/us/")
button = browser.find_element_by_xpath("//*[@id="stations"]/li[1]/button")
button.click()