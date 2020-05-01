from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

import datetime

wgSite = 'https://www.windguru.cz/station/42'

def scrapeWG(browser, wait, collection):

    browser.get(wgSite)

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//span[@class='wgs_wind_avg_value']")))

    avg = float(browser.find_element_by_xpath(
        "//span[@class='wgs_wind_avg_value']").text)
    low = float(browser.find_element_by_xpath(
        "//span[@class='wgs_wind_min_value']").text)
    high = float(browser.find_element_by_xpath(
        "//span[@class='wgs_wind_max_value']").text)
    direction = browser.find_element_by_xpath(
        "//span[@class='wgs_wind_dir_value']").text

    timestamp = datetime.datetime.utcnow()

    record = {"date": timestamp, "avg": avg, "low": low, "high": high, "direction": direction}

    collection.insert_one(record)

    print("added wind record")
