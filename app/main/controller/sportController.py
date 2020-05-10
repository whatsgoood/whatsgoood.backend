from flask import jsonify
from os import environ
import pymongo

from app.main.service import sportService, weatherService
from app.main.model import weatherEvalModel
from app.main.sportEvaluator.sportEvaluator import weight

ws = weatherService()
ss = sportService()

def sportList():

    sportList = ss.getSupportedSports()

    outSportList = []

    for sport in sportList: 

        #TODO: create getEvalModel method on weatherService

        weatherModel = weatherEvalModel(
                windHigh = 5.0,
                windLow = 2.0,
                windAvg = 3.0,
                windDirection = "W",

                waveSize = 8.5,
                wavePeriod = 10,

                cloudCover = 0.0,
                temparature = 15,
                chanceOfRain = 0.0,
            ).__dict__


        outSportList.append(
            {
                "name": sport,
                "rating": weight(weatherModel, sport)
            }
        )

    return jsonify(outSportList)