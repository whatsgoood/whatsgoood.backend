from os import environ
import pymongo
from app.main.service import sportService, weatherService
from app.main.dankOMeter import dankOMeter
from app.main.model import weatherEvalModel
from flask import jsonify

ws = weatherService()
ss = sportService()

def sportList():

    sportList = []

    latestLiveWind = ws.getWindInfo()[1]
    latestLiveWaves = ws.getWaveInfo()[1]

    wem = weatherEvalModel(
        windHigh = latestLiveWind.high,
        windLow = latestLiveWind.low,
        windAvg = latestLiveWind.avg,
        windDirection = latestLiveWind.direction,

        waveSize = latestLiveWaves.size,
        wavePeriod = latestLiveWaves.period

        # cloudCover =
        # temparature =
        # chanceOfRain =
    )
    
    d = dankOMeter()

    for sport in ss.getSupportedSports():
        sportList.append(
            {
                "name": sport,
                "rating": d.getRating(sport, wem)
            }
        )

    return jsonify(sportList)