from datetime import datetime
from app.models import waveDBModel, windDBModel, climateDBModel, weatherSummaryModel
from app import app, db

from flask import Blueprint, abort, jsonify
from flask_cors import CORS

weather_bp = Blueprint('weather', __name__)
CORS(weather_bp)

forecastHours = app.config['FORECASTHOURS']

windModels = None
waveModels = None
climateModels = None

lastUpdatedTime = None


def updateWeatherModels():
    global lastUpdatedTime

    if lastUpdatedTime is None or ((datetime.now() - lastUpdatedTime).seconds / 60) > 15:

        now = datetime.now()
        time = datetime(now.year, now.month, now.day, 6, 0, 0)

        global windModels
        global waveModels
        global climateModels

        windModels = windForecastInfo(time)
        waveModels = waveForecastInfo(time)
        climateModels = climateForecastInfo(time)

        lastUpdatedTime = now


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


@weather_bp.route("/weather/forecast")
def get_forecastWeather():

    forecastWeather = []

    updateWeatherModels()

    for time in getForecastTimes():

        windModel = windInfo(time)
        waveModel = waveInfo(time)
        climateModel = climateInfo(time)

        if windModel is None or waveModel is None or climateModel is None:
            forecastWeatherModel = {"Error": f"Incomplete forecast data for time: {time}"}
            forecastWeather.append(forecastWeatherModel)
            continue

        forecastWeatherModel = {
            "time": time,
            "windInfo": windModel.__dict__,
            "waveInfo": waveModel.__dict__,
            "climateInfo": climateModel.__dict__
        }

        forecastWeather.append(forecastWeatherModel)

    return jsonify(forecastWeather)


@weather_bp.route("/weather/forecast/<hour>")
def get_forecastWeather_hourly(hour):

    now = datetime.now()
    time = datetime(now.year, now.month, now.day, int(hour), 0, 0)

    updateWeatherModels()

    windModel = windInfo(time)
    waveModel = waveInfo(time)
    climateModel = climateInfo(time)

    if windModel is None or waveModel is None or climateModel is None:
        forecastWeatherModel = {"Error": f"Incomplete forecast dataset for time: {time}"}
    else:
        forecastWeatherModel = {
            "time": time,
            "windInfo": windModel.__dict__,
            "waveInfo": waveModel.__dict__,
            "climateInfo": climateModel.__dict__
        }

    return forecastWeatherModel


def climateForecastInfo(startTime):

    climateInfo_Cursor = db.climateForecastCollection.find({
        "forecastTime": {
            '$gte': startTime
        }
    })

    climateInfo = list(climateInfo_Cursor)
    return climateInfo


def climateInfo(time=None):

    climateModel = None

    if time is None:    # live
        climateInfo_Cursor = db.climateCollection.find({})
        climateInfo = list(climateInfo_Cursor)[-1]
        climateModel = climateDBModel(climateInfo)
    else:               # forecast
        for model in climateModels:
            if model['forecastTime'] == time:
                climateModel = climateDBModel(model)
                break

    return climateModel or None


def waveForecastInfo(startTime):

    waveInfo_Cursor = db.waveForecastCollection.find({
        "forecastTime": {
            '$gte': startTime
        }
    })

    waveInfo = list(waveInfo_Cursor)

    return waveInfo


def waveInfo(time=None):

    waveModel = None

    if time is None:    # live
        waveInfo_Cursor = db.wavesCollection.find({})
        waveInfo = list(waveInfo_Cursor)[-1]
        waveModel = waveDBModel(waveInfo)
    else:               # forecast
        for model in waveModels:
            if model['forecastTime'] == time:
                waveModel = waveDBModel(model)
                break

    return waveModel or None


def windForecastInfo(startTime):

    windInfo_Cursor = db.windForecastCollection.find({
        "forecastTime": {
            '$gte': startTime
        }
    })

    windInfo = list(windInfo_Cursor)
    return windInfo


def windInfo(time=None):

    windModel = None

    if time is None:    # live
        windInfo_Cursor = db.windCollection.find({})
        windInfo = list(windInfo_Cursor)[-1]
        windModel = windDBModel(windInfo)
    else:               # forecast
        for model in windModels:
            if model['forecastTime'] == time:
                windModel = windDBModel(model)
                break

    return windModel


def getForecastTimes():

    now = datetime.now()
    forecastTimes = []

    for hour in forecastHours:
        date = datetime(now.year, now.month, now.day, hour, 0, 0)
        forecastTimes.append(date)

    return forecastTimes


def evalModel(time=None):

    weatherSummary = weatherSummaryModel({
        "windInfo": windInfo(time),
        "waveInfo": waveInfo(time),
        "climateInfo": climateInfo(time)
    })

    return weatherSummary
