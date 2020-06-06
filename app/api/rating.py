from app.sportEvaluator import weight
from app.api.weather import liveWeather
from app.models import weatherSummaryModel, weatherEvalModel
from flask import Blueprint, jsonify
from flask_cors import CORS

rating_bp = Blueprint('rating', __name__)
CORS(rating_bp)

@rating_bp.route('/ratings')
def get_ratings():

    weatherSummaryDict = liveWeather().__dict__

    weatherSummary = weatherSummaryModel(weatherSummaryDict)

    # region Seed
    # evaluationModel = weatherEvalModel(

    #     windHigh=10.0,
    #     windLow=3.0,
    #     windAvg=5.0,
    #     windDirection="W",

    #     waveSize=7.0,
    #     wavePeriod=12,

    #     cloudCover=0,
    #     temparature=15,
    #     rain=0.0

    # ).__dict__

    # endregion

    evaluationModel = weatherEvalModel(

        windHigh=float(weatherSummary.windInfo.high),
        windLow=float(weatherSummary.windInfo.low),
        windAvg=float(weatherSummary.windInfo.avg),
        windDirection=weatherSummary.windInfo.direction,

        waveSize=float(weatherSummary.waveInfo.waveSize),
        wavePeriod=float(weatherSummary.waveInfo.wavePeriod),

        cloudCover=float(weatherSummary.climateInfo.cloudcover),
        temparature=float(weatherSummary.climateInfo.temp),
        rain=float(weatherSummary.climateInfo.rain)

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
