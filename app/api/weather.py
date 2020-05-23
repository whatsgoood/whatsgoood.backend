from app.models import waveDBModel, windDBModel, climateDBModel, weatherSummaryModel
from app import db

from flask import Blueprint

weather_bp = Blueprint('weather', __name__)


@weather_bp.route('/weather/live')
def get_liveWeather():

    weatherSummary = weatherSummaryModel({
        "windInfo": get_windInfo(),
        "waveInfo": get_waveInfo(),
        "climateInfo": get_climateInfo()
    })

    return weatherSummary.__dict__


def liveWeather():

    weatherSummary = weatherSummaryModel({
        "windInfo": windInfo(),
        "waveInfo": waveInfo(),
        "climateInfo": climateInfo()
    })

    return weatherSummary


@weather_bp.route('/weather/live/climate')
def get_climateInfo():

    return climateInfo().__dict__


def climateInfo():

    climateInfo_Cursor = db.climateCollection.find({})

    latestClimateInfo = list(climateInfo_Cursor)[-1]

    climateModel = climateDBModel(latestClimateInfo)

    return climateModel


@weather_bp.route('/weather/live/waves')
def get_waveInfo():

    return waveInfo().__dict__


def waveInfo():

    waveInfo_Cursor = db.wavesCollection.find({})

    latestWaveInfo = list(waveInfo_Cursor)[-1]

    waveModel = waveDBModel(latestWaveInfo)

    return waveModel


@weather_bp.route('/weather/live/wind')
def get_windInfo():

    return windInfo().__dict__


def windInfo():

    windInfo_Cursor = db.windCollection.find({})

    latestWindInfo = list(windInfo_Cursor)[-1]

    windModel = windDBModel(latestWindInfo)

    return windModel
