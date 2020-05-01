from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

from mswScraper import scrapeMSW
from wgScraper import scrapeWG

import datetime
from os import environ
import schedule
import pymongo
import time

options = webdriver.ChromeOptions()
options.add_argument(
    "user-data-dir=C:\\Users\\kritz\\AppData\\Local\\Google\\Chrome\\Selenium Data")

browser = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
wait = WebDriverWait(browser, 10)

mongoUrl = environ.get('WHATSGOOD_CONSTR')

client = pymongo.MongoClient(mongoUrl)
db = client['plagiarismDB']

windCol = db['windCollection']
wavesCol = db['wavesCollection']

windCol.create_index("date", expireAfterSeconds=(2 * 86400))  # 2 days
wavesCol.create_index("date", expireAfterSeconds=(2 * 86400))  # 2 days


def delegateCalls(browser, wait):

    timeCalled = datetime.datetime.now().minute

    if timeCalled == 0:
        scrapeMSW(browser, wait, wavesCol)

    if timeCalled in [0, 15, 30, 45]:
        scrapeWG(browser, wait, windCol)


trigger = CronTrigger(hour='6-20', minute="0,15,30,45")

scheduler = BlockingScheduler()
scheduler.add_job(lambda: delegateCalls(browser, wait), trigger=trigger)
scheduler.start()
