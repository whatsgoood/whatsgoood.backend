from os import environ
import pymongo
from app.main.service import weatherService

ws = weatherService()

def weatherSummary():

    latestLiveWind = ws.getWindInfo()[1]

    output = {
        "latestWindReading" : {
            "avg": latestLiveWind.avg,
            "low":latestLiveWind.low,
            "high":latestLiveWind.high,
            "direction":latestLiveWind.direction
        }
    }

    return output