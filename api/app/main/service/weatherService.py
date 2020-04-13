import os
from app.main import dbContext
from app.main.model import windModel, waveModel

class weatherService():

    def __init__(self):
        self.db = dbContext()
        
    def getWindInfo(self):

        windModels = []

        for wm in list(self.db.windCol.find({})):
            windModels.append(
                windModel(
                    high = wm['high'],
                    low = wm['low'],
                    avg = wm['avg'],
                    direction = wm['direction']
                )
            )

        return windModels

    def getWaveInfo(self):

        waveModels = []

        for wm in list(self.db.waveCol.find({})):
            waveModels.append(
                waveModel(
                    size = wm['waveSize'],
                    period = wm['wavePeriod']
                )
            )

        return waveModels

    # return list(self.db.waveCol.find({}))

# def getWeatherInfo(self):
#     return list(db.weatherCol.find({}))

