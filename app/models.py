from app import db


class sportModel:

    name = "Default"
    rating = 0.0

    def __init__(self, name, rating):
        self.name = name
        self.rating = rating


class waveModel():

    size = 0.0
    period = 0.0

    def __init__(self, size, period):
        self.size = size
        self.period = period


class weatherEvalModel():

    windHigh = 0.0
    windLow = 0.0
    windAvg = 0.0
    windDirection = "Default"

    waveSize = 0.0
    wavePeriod = 0.0

    cloudCover = 0.0
    temparature = 0.0
    chanceOfRain = 0.0

    def __init__(self, windHigh=None, windLow=None, windAvg=None, windDirection=None, waveSize=None, wavePeriod=None, cloudCover=None, temparature=None, chanceOfRain=None):
        self.windHigh = windHigh
        self.windLow = windLow
        self.windAvg = windAvg
        self.windDirection = windDirection

        self.waveSize = waveSize
        self.wavePeriod = wavePeriod

        self.cloudCover = cloudCover
        self.temparature = temparature
        self.chanceOfRain = chanceOfRain


class windModel():

    high = 0.0
    low = 0.0
    avg = 0.0
    direction = "Default"

    def __init__(self, high, low, avg, direction):
        self.high = high
        self.low = low
        self.avg = avg
        self.direction = direction
