from app.sportEvaluator import getRatingModel
from app.api.weather import evalModel
from app.models import weatherSummaryModel, weatherEvalModel
from flask import Blueprint, jsonify, abort
from flask_cors import CORS
from app import app

rating_bp = Blueprint('rating', __name__)
CORS(rating_bp)

supportedSports = app.config['SPORTS']

@rating_bp.route('/ratings/<sport>')
def get_rating(sport):

    if sport.lower() not in supportedSports:
        return abort(404, "We don't do that here")

    evaluationModel = createEvalModel()

    ratingModel = getRatingModel(evaluationModel, sport)

    return ratingModel



@rating_bp.route('/ratings')
def get_ratings():

    evaluationModel = createEvalModel()

    outSportList = []

    for sport in supportedSports:

        ratingModel = getRatingModel(evaluationModel, sport)

        outSportList.append(ratingModel)

    return jsonify(outSportList)

def createEvalModel():

    weatherSummary = evalModel()

    # region Seed
    # evalulationModel = weatherEvalModel(

    #     windHigh=10.0,
    #     windLow=3.0,
    #     windAvg=5.0,
    #     windDirection="W",

    #     waveSize=7.0,
    #     wavePeriod=12,

    #     cloudCover=0,
    #     temperature=15,
    #     rain=0.0

    # ).__dict__

    # endregion

    evalulationModel = weatherEvalModel(

        windHigh=float(weatherSummary.windInfo.high),
        windLow=float(weatherSummary.windInfo.low),
        windAvg=float(weatherSummary.windInfo.avg),
        windDirection=weatherSummary.windInfo.direction,

        waveSize=float(weatherSummary.waveInfo.waveSize),
        wavePeriod=float(weatherSummary.waveInfo.wavePeriod),

        cloudCover=float(weatherSummary.climateInfo.cloudcover),
        temperature=float(weatherSummary.climateInfo.temp),
        rain=float(weatherSummary.climateInfo.rain)

    ).__dict__

    return evalulationModel
