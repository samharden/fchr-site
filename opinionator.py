"""
    Purpose: to scrape through and save the DOAH opinions into one place.
    Needs:
        the save_opinion function isn't working
        should iterate through every page
"""



import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import os
import urllib3
import re
from bs4 import BeautifulSoup
import urllib
#Gets to the criminal and traffic search pages:
	##Key:	ID=100 	:	Criminal
	##		ID=200	:	Probate
	##		ID=300	:	All case types
	##		ID=400	:	Civil & Family
driver = webdriver.Chrome("/Library/Python/chromedriver")
driver.get('https://www.doah.state.fl.us/ROS/')

page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')
pretty_soup = soup.prettify()

tags = soup('a')
# print case_text
list1=list()
for tag in tags:
  x = tag.get('href', None)
  list1.append(x)

print(list1)

for link in list1[:2]:
    driver.get("https://www.doah.state.fl.us/"+link.rstrip())
    # print(driver.page_source)

    opinion_list=list()
    opinion_page = driver.page_source
    opinion_soup = BeautifulSoup(opinion_page, 'html.parser')

    opinions = opinion_soup('a')
    i = 0
    ##Work in progress here ...
    for opinion in opinions:
        o = opinion.get('href', None)
        opinion_list.append(o)
        i =+ 1
        source = str(driver.page_source)
        def save_opinion(obj, filename):
            with open(filename, 'w') as output:
                try:
                    pickle.dump(obj, output, -1)
                    os.chdir('/dir/to/save/opinions')
                except Exception as inst:
                    print(type(inst))
                    print(inst.args)
                    print(inst)
        save_opinion(source, 'Opinion %i.pdf' % i)
