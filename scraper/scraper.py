from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pymongo
from os import environ

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\kritz\\AppData\\Local\\Google\\Chrome\\Selenium Data")

browser = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
browser.implicitly_wait(2)

macWindSite = 'https://mac-wind.appspot.com/'

mongoUrl = f"mongodb+srv://{environ.get('MONGO_USER')}:{environ.get('MONGO_KEY')}@sandboxcluster-xg5gf.mongodb.net/test?retryWrites=true&w=majority"

client = pymongo.MongoClient(mongoUrl)
db = client['plagiarismDB']
macWindCol = db['macWindCollection']

while True:
    browser.get(macWindSite)
    topRow = browser.find_elements_by_xpath("(//tr)[2]/td")
    avg = float(topRow[0].text)
    low = float(topRow[1].text)
    high = float(topRow[2].text)
    direction = topRow[3].text

    print(f"{{ avg: {avg}, low : {low}, high : {high}, direction : {direction} }}")

    macWindCol.insert_one({ "avg": avg, "low" : low, "high" : high, "direction" : direction})

    time.sleep(1)
