from app.sportEvaluator import getRatingModel
from app.api.weather import evalModel
from app.models import weatherSummaryModel, weatherEvalModel
from flask import Blueprint, jsonify, abort, request
from datetime import datetime
from flask_cors import CORS
from app import app

rating_bp = Blueprint('rating', __name__)
CORS(rating_bp)

supportedSports = app.config['SPORTS']
forecastHours = app.config['FORECASTHOURS']


@rating_bp.route('/ratings/live/<sport>')
def get_rating(sport):

    if sport.lower() not in supportedSports:
        return abort(404, "We don't do that here")

    evaluationModel = createEvalModel(evalModel())

    ratingModel = getRatingModel(evaluationModel, sport)

    return ratingModel


@rating_bp.route('/ratings/live')
def get_ratings():

    evaluationModel = createEvalModel(evalModel())

    outSportList = []

    for sport in supportedSports:

        ratingModel = getRatingModel(evaluationModel, sport)

        outSportList.append(ratingModel)

    return jsonify(outSportList)


@rating_bp.route('/ratings/forecast')
def get_ratingsForecast():
    sport = request.args.get('sport')
    hour = request.args.get('hour')

    forecastWeather = []
    ratingList = []
    ratingsForecastOutput = {}

    if not hour:
        #  all hours
        for time in getForecastTimes():

            forecastEvalModel = evalModel(time)

            if forecastEvalModel.windInfo is None or forecastEvalModel.waveInfo is None or forecastEvalModel.climateInfo is None:
                forecastWeatherModel = {
                    "Error": "Incomplete forecast dataset",
                    "time": time
                }
            else:
                forecastWeatherModel = {
                    "time": time,
                    "windInfo": forecastEvalModel.windInfo.__dict__,
                    "waveInfo": forecastEvalModel.waveInfo.__dict__,
                    "climateInfo": forecastEvalModel.climateInfo.__dict__,
                    "Error": None
                }

            forecastWeather.append(forecastWeatherModel)

    else:
        #  one hour
        now = datetime.now()
        time = datetime(now.year, now.month, now.day, int(hour), 0, 0)
        forecastEvalModel = evalModel(time)

        if forecastEvalModel.windInfo is None or forecastEvalModel.waveInfo is None or forecastEvalModel.climateInfo is None:
            forecastWeatherModel = {
                "Error": "Incomplete forecast dataset",
                "time": time
            }
        else:
            forecastWeatherModel = {
                "time": time,
                "windInfo": forecastEvalModel.windInfo.__dict__,
                "waveInfo": forecastEvalModel.waveInfo.__dict__,
                "climateInfo": forecastEvalModel.climateInfo.__dict__,
                "Error": None
            }

        forecastWeather.append(forecastWeatherModel)

    if not sport:
        #  all sports
        for forecastWeatherObject in forecastWeather:

            if forecastWeatherObject['Error'] is not None:
                ratingList = [forecastWeatherObject]
            else:
                for sport in supportedSports:

                    evaluationModel = createEvalModel(
                        evalModel(forecastWeatherObject['time']))

                    ratingModel = getRatingModel(evaluationModel, sport)

                    ratingList.append(ratingModel)

            ratingsForecastOutput[forecastWeatherObject['time'].hour] = ratingList
            ratingList = []

    else:
        #  one sport
        for forecastWeatherObject in forecastWeather:

            if forecastWeatherObject['Error'] is not None:
                ratingList = [forecastWeatherObject]
            else:

                evaluationModel = createEvalModel(
                    evalModel(forecastWeatherObject['time']))

                ratingModel = getRatingModel(evaluationModel, sport)

                ratingList = [ratingModel]

            ratingsForecastOutput[forecastWeatherObject['time'].hour] = ratingList
            ratingList = []

    return jsonify(ratingsForecastOutput)


def createEvalModel(weatherSummary):

    # region Seed
    # evalulationModel = weatherEvalModel(

    #     windHigh=10.0,
    #     windLow=3.0,
    #     windAvg=5.0,
    #     windDirection="W",

    #     waveSize=7.0,
    #     wavePeriod=12,
    #     twoDayAvg=5.0,

    #     cloudCover=0,
    #     temperature=15,
    #     rain=0.0,
    #     rain12h = 0.0

    # ).__dict__

    # endregion

    evalulationModel = weatherEvalModel(

        windHigh=float(weatherSummary.windInfo.high),
        windLow=float(weatherSummary.windInfo.low),
        windAvg=float(weatherSummary.windInfo.avg),
        windDirection=weatherSummary.windInfo.direction,

        waveSize=float(weatherSummary.waveInfo.waveSize),
        wavePeriod=float(weatherSummary.waveInfo.wavePeriod),
        twoDayAvg=float(weatherSummary.waveInfo.twoDayAvg),

        cloudCover=float(weatherSummary.climateInfo.cloudcover),
        temperature=float(weatherSummary.climateInfo.temp),
        rain=float(weatherSummary.climateInfo.rain),
        rain12h=float(weatherSummary.climateInfo.rain12h)

    ).__dict__

    return evalulationModel


def getForecastTimes():

    now = datetime.now()
    forecastTimes = []

    for hour in forecastHours:
        date = datetime(now.year, now.month, now.day, hour, 0, 0)
        forecastTimes.append(date)

    return forecastTimes
