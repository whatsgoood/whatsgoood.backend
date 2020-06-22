from app.models import waveDBModel, windDBModel, climateDBModel, weatherSummaryModel
from app import db

from flask import Blueprint, abort
from flask_cors import CORS

weather_bp = Blueprint('weather', __name__)
CORS(weather_bp)


@weather_bp.route('/weather/live')
def get_liveWeather():

    weatherSummary = weatherSummaryModel({
        "windInfo": windInfo().__dict__,
        "waveInfo": waveInfo().__dict__,
        "climateInfo": climateInfo().__dict__
    })

    return weatherSummary.__dict__

@weather_bp.route('/weather/live/<model>')
def get_weatherModels(model):

    key = model.lower() + "Info"

    liveWeatherModel = get_liveWeather()

    if key in liveWeatherModel:
        return liveWeatherModel[key]
    else:
        return abort(404, "Invalid weather info requested")


def climateInfo():

    climateInfo_Cursor = db.climateCollection.find({})

    latestClimateInfo = list(climateInfo_Cursor)[-1]

    climateModel = climateDBModel(latestClimateInfo)

    return climateModel


def waveInfo():

    waveInfo_Cursor = db.wavesCollection.find({})

    latestWaveInfo = list(waveInfo_Cursor)[-1]

    waveModel = waveDBModel(latestWaveInfo)

    return waveModel


def windInfo():

    windInfo_Cursor = db.windCollection.find({})

    latestWindInfo = list(windInfo_Cursor)[-1]

    windModel = windDBModel(latestWindInfo)

    return windModel

def evalModel():

    weatherSummary = weatherSummaryModel({
        "windInfo": windInfo(),
        "waveInfo": waveInfo(),
        "climateInfo": climateInfo()
    })

    return weatherSummary