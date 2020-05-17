# from api import weatherService
from flask import jsonify
from flask import Blueprint

weather_bp = Blueprint('weather', __name__)

# ws = weatherService()


@weather_bp.route('/weather')
def weather():

    # latestLiveWind = ws.getWindInfo()[1]

    # weatherSummary = {
    #     "avg": latestLiveWind.avg,
    #     "low": latestLiveWind.low,
    #     "high": latestLiveWind.high,
    #     "direction": latestLiveWind.direction
    # }

    # return jsonify(weatherSummary)
    return "test"
