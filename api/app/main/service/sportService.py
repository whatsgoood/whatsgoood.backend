import os
from app.main import dbContext
from app.main import config
from app.main.model import windModel

class sportService():

    supportedSports = config.sports

    def __init__(self):
        self.db = dbContext()

    def getSupportedSports(self):

        return self.supportedSports