from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

import time
import pymongo
from os import environ

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\kritz\\AppData\\Local\\Google\\Chrome\\Selenium Data")

browser = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
wait = WebDriverWait(browser, 10)

macWindSite = 'https://mac-wind.appspot.com/'

mongoUrl = environ.get('WHATSGOOD_CONSTR')

client = pymongo.MongoClient(mongoUrl)
db = client['plagiarismDB']
windCol = db['windCollection']

while True:
    browser.get(macWindSite)
    wait.until(ec.visibility_of_element_located((By.XPATH, "(//tr)[2]/td")))
    
    topRow = browser.find_elements_by_xpath("(//tr)[2]/td")
    avg = float(topRow[0].text)
    low = float(topRow[1].text)
    high = float(topRow[2].text)
    direction = topRow[3].text

    print(f"{{ avg: {avg}, low : {low}, high : {high}, direction : {direction} }}")

    windCol.insert_one({ "avg": avg, "low" : low, "high" : high, "direction" : direction})

    time.sleep(1)
