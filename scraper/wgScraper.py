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

wgSite = 'https://www.windguru.cz/station/42'

mongoUrl = environ.get('WHATSGOOD_CONSTR')

client = pymongo.MongoClient(mongoUrl)
db = client['plagiarismDB']
windCol = db['windCollection']

while True:
    browser.get(wgSite)

    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='wgs_wind_avg_value']")))

    avg = float(browser.find_element_by_xpath("//span[@class='wgs_wind_avg_value']").text)
    low = float(browser.find_element_by_xpath("//span[@class='wgs_wind_min_value']").text)
    high = float(browser.find_element_by_xpath("//span[@class='wgs_wind_max_value']").text)
    direction = browser.find_element_by_xpath("//span[@class='wgs_wind_dir_value']").text

    print(f"{{ avg: {avg}, low : {low}, high : {high}, direction : {direction} }}")

    windCol.insert_one({ "avg": avg, "low" : low, "high" : high, "direction" : direction})

    time.sleep(1)