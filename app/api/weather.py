from datetime import datetime, timedelta
from app.models import waveDBModel, windDBModel, climateDBModel, weatherSummaryModel
from app import app, db

from flask import Blueprint, abort, jsonify
from flask_cors import CORS

weather_bp = Blueprint('weather', __name__)
CORS(weather_bp)

forecastHours = app.config['FORECASTHOURS']

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

def getForecastTimes():

    now = datetime.now()
    forecastTimes = []

    for hour in forecastHours:
        date = datetime(now.year, now.month, now.day, hour, 0, 0)
        forecastTimes.append(date)

    return forecastTimes


def climateInfo(time=None):

    if time is None:

        climateInfo_Cursor = db.climateCollection.find({})

        climateInfo = list(climateInfo_Cursor)[-1]

        climateModel = climateDBModel(climateInfo)

        return climateModel

    else:

        climateInfo_Cursor = db.climateForecastCollection.find({
            "forecastTime": {
                '$gte': time,
                '$lt': time + timedelta(hours=1)
            }
        })

        try:

            climateInfo = list(climateInfo_Cursor)[0]
            climateModel = climateDBModel(climateInfo)
            return climateModel

        except IndexError:
            return None


def waveInfo(time=None):

    if time is None:

        waveInfo_Cursor = db.wavesCollection.find({})

        waveInfo = list(waveInfo_Cursor)[-1]

        waveModel = waveDBModel(waveInfo)

        return waveModel

    else:

        waveInfo_Cursor = db.waveForecastCollection.find({
            "forecastTime": {
                '$gte': time,
                '$lt': time + timedelta(hours=1)
            }
        })

        try:
            waveInfo = list(waveInfo_Cursor)[0]
            waveModel = waveDBModel(waveInfo)
            return waveModel

        except IndexError:
            return None


def windInfo(time=None):

    if time is None:

        windInfo_Cursor = db.windCollection.find({})

        windInfo = list(windInfo_Cursor)[-1]

        windModel = windDBModel(windInfo)

        return windModel

    else:

        windInfo_Cursor = db.windForecastCollection.find({
            "forecastTime": {
                '$gte': time,
                '$lt': time + timedelta(hours=1)
            }
        })

        try:

            windInfo = list(windInfo_Cursor)[0]
            windModel = windDBModel(windInfo)
            return windModel

        except IndexError:
            return None


def evalModel():

    weatherSummary = weatherSummaryModel({
        "windInfo": windInfo(),
        "waveInfo": waveInfo(),
        "climateInfo": climateInfo()
    })

    return weatherSummary
