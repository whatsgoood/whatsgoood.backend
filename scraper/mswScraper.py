from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

import math
import time
import datetime

import pymongo
from os import environ

options = webdriver.ChromeOptions()
options.add_argument(
    "user-data-dir=C:\\Users\\kritz\\AppData\\Local\\Google\\Chrome\\Selenium Data")

browser = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
wait = WebDriverWait(browser, 10)

mswSite = 'https://magicseaweed.com/Cape-Town-Surf-Report/81/'

mongoUrl = environ.get('WHATSGOOD_CONSTR')

client = pymongo.MongoClient(mongoUrl)
db = client['plagiarismDB']
wavesCol = db['wavesCollection']

wavesCol.create_index("date", expireAfterSeconds=(2 * 86400))  # 2 days

while True:
    browser.get(mswSite)
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//tr[@data-forecast-day='1']")))

    wavesTable = browser.find_elements_by_xpath(
        "//tr[@data-forecast-day='1']")[2:]

    now = datetime.datetime.now().time().hour

    percent = (now / 24)

    closestRowIndex = round(6 * percent) - 1

    liveRow = wavesTable[closestRowIndex]

    waveDetails = liveRow.find_elements_by_xpath(
        ".//td/h4[@class='nomargin font-sans-serif heavy']")

    waveSize = float(waveDetails[0].text[:-2])
    wavePeriod = float(waveDetails[1].text[:-1])
    timestamp = datetime.datetime.utcnow()

    wavesCol.insert_one({"date": timestamp, "waveSize": waveSize, "wavePeriod": wavePeriod})

    time.sleep(2)
