from Models.dankOMeter import dankOMeter
from flask import Flask
from os import environ
import pymongo
import config

app = Flask(__name__)

mongoUrl = environ.get('WHATSGOOD_CONSTR')

client = pymongo.MongoClient(mongoUrl)
db = client['plagiarismDB']
wgCol = db['windGuruCollection']


@app.route("/api/getWeatherSummary")
def weatherSummary():

    latestLiveWind = list(wgCol.find({}))[-1]

    output = {
        "latestWindReading" : {
            "avg": latestLiveWind['avg'],
            "low":latestLiveWind['low'],
            "high":latestLiveWind['high'],
            "dir":latestLiveWind['direction']
        }
    }

    return output


@app.route("/api/getActivityList")
def activityList():

    activityList = []

    latestLiveWind = list(wgCol.find({}))[-1]

    weatherObj = {
        "latestWindReading": latestLiveWind
    }
    
    d = dankOMeter()

    for sport in config.sports:
        activityList.append(
            {
                "sport": sport,
                "rating": d.getRating(sport, weatherObj)
            }
        )

    return {
        "activitySummary": activityList
    }


if __name__ == "__main__":
    app.run()