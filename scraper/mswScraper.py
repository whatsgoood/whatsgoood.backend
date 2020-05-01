from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

import datetime

mswSite = 'https://magicseaweed.com/Cape-Town-Surf-Report/81/'

def scrapeMSW(browser, wait, collection):

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

    record = {"date": timestamp, "waveSize": waveSize, "wavePeriod": wavePeriod}

    collection.insert_one(record)

    print("added wave record")