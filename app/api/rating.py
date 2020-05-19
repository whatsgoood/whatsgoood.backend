from app.sportEvaluator import weight
from app.api.weather import liveWeather
from app.models import weatherSummaryModel, weatherEvalModel
from flask import Blueprint, jsonify

rating_bp = Blueprint('rating', __name__)

@rating_bp.route('/ratings')
def get_ratings():

    weatherSummaryDict = liveWeather().__dict__

    weatherSummary = weatherSummaryModel(weatherSummaryDict)

    test = weatherSummary.windInfo.high

    # region Seed
    # evaluationModel = weatherEvalModel(

    #     windHigh=35.0,
    #     windLow=20.0,
    #     windAvg=27.0,
    #     windDirection="SSE",

    #     waveSize=6.0,
    #     wavePeriod=12,

    #     cloudCover=0,
    #     temparature=25,
    #     chanceOfRain=0.0

    # ).__dict__

    #endregion

    evaluationModel = weatherEvalModel(

        windHigh=float(weatherSummary.windInfo.high),
        windLow=float(weatherSummary.windInfo.low),
        windAvg=float(weatherSummary.windInfo.avg),
        windDirection=weatherSummary.windInfo.direction,

        waveSize=float(weatherSummary.waveInfo.size),
        wavePeriod=float(weatherSummary.waveInfo.period),

        cloudCover=float(weatherSummary.climateInfo.cloudcover),
        temparature=float(weatherSummary.climateInfo.temp),
        chanceOfRain=0.0

    ).__dict__

    sportList = [
        "Kiting",
        "Climbing",
        "Surfing"
    ]

    outSportList = []

    for sport in sportList:

        outSportList.append(
            {
                "name": sport,
                "rating": weight(evaluationModel, sport)
            }
        )

    return jsonify(outSportList)
