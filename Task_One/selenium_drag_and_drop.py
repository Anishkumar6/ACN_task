import time
import pandas as pd
from argparse import ArgumentParser
import argparse
from selenium import webdriver as wd
import selenium
import numpy as np
#from schema import SCHEMA
import json
import urllib
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.common.action_chains import ActionChains
import subprocess



#Initialising Chrome Driver
chrome_options = wd.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('log-level=3')
browser = wd.Chrome(options=chrome_options)
#Path to chrome driver
browser.get(r"C:\Users\inankum29\Desktop\index_acn.html")
#Initialising List order
jab_code_order = ['J92.9','A10.2','E24.9','B10.2','F19.10','D10.11']
#Movement of first element
source_element = browser.find_element_by_xpath('//td[text()="J92.9"]//ancestor::tr//td[1]')
dest_element   = browser.find_element_by_xpath('//tbody[@id="sortable"]//tr[1]')
ActionChains(browser).drag_and_drop(source_element, dest_element).perform()

#Dynamically moving of remain elements as per order in list
for i in range(1,len(jab_code_order)):
    so_addr        = '//td[text()="'+str(jab_code_order[i])+'"]//ancestor::tr//td[1]'
    dest_addr      = '//td[text()="'+str(jab_code_order[i-1])+'"]/following::tr[1]//td[1]'
    source_element = browser.find_element_by_xpath(so_addr)
    dest_element   = browser.find_element_by_xpath(dest_addr)
    ActionChains(browser).drag_and_drop(source_element, dest_element).perform()



