from app import app
from app.main.controller import weatherController, sportController
from app.main.db import dbCleaner
import atexit

@app.route("/api/getWeatherSummary")
def getWeatherSummary():
    return weatherController.weatherSummary()


@app.route("/api/getSportList")
def getSportList():
    return sportController.sportList()


def run():
    dbC = dbCleaner()
    atexit.register(lambda: dbC.scheduler.shutdown())
    app.run()

if __name__ == '__main__':
    run()