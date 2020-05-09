from app import app
from app.main.controller import weatherController, sportController

@app.route("/api/getWeatherSummary")
def getWeatherSummary():
    return weatherController.weatherSummary()


@app.route("/api/getSportList")
def getSportList():
    return sportController.sportList()


def run():
    app.run()

if __name__ == '__main__':
    run()