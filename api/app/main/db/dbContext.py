from os import environ
import pymongo

from apscheduler.schedulers.background import BackgroundScheduler
import time

class dbContext:

    windCol = []
    waveCol = []
    weatherCol = []

    def __init__(self):
        mongoUrl = environ.get('WHATSGOOD_CONSTR')
        client = pymongo.MongoClient(mongoUrl)
        db = client['plagiarismDB']

        self.windCol = db['windCollection']
        self.waveCol = db['wavesCollection']
        self.weatherCol = db['weatherCollection']
