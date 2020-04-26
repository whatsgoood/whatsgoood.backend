from os import environ
import pymongo

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import time

class dbCleaner():

    def __init__(self):

        self.scheduler = BackgroundScheduler()
        t = CronTrigger(hour='20', minute='0')
        self.scheduler.add_job(func=self.cleandb, trigger=t)

        self.scheduler.start()

    def cleandb(self):

        print("cleaningdb")
        # mongoUrl = environ.get('WHATSGOOD_CONSTR')
        # client = pymongo.MongoClient(mongoUrl)
        # db = client['plagiarismDB']

        # self.windCol = db['windCollection']
        # self.waveCol = db['wavesCollection']
        # self.weatherCol = db['weatherCollection']
