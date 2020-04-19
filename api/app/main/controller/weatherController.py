from os import environ
import pymongo
from app.main.service import weatherService
from flask import jsonify

ws = weatherService()

def weatherSummary():

    latestLiveWind = ws.getWindInfo()[1]
    
    weatherSummary = {
        "avg": latestLiveWind.avg,
        "low":latestLiveWind.low,
        "high":latestLiveWind.high,
        "direction":latestLiveWind.direction
    }

    return jsonify(weatherSummary)
