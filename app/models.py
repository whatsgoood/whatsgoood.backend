from collections import namedtuple


class windDBModel:

    high = 0.0
    low = 0.0
    avg = 0.0
    direction = "Default"

    def __init__(self, dictionary):
        for k, v in dictionary.items():
            if k != "_id":
                setattr(self, k, v)


class waveDBModel:

    waveSize = 0.0
    wavePeriod = 0.0

    def __init__(self, dictionary):
        for k, v in dictionary.items():
            if k != "_id":
                setattr(self, k, v)


class climateDBModel:

    temp = 0.0
    cloudCover = 0.0
    Description = ""
    rain = 0.0

    def __init__(self, dictionary):
        for k, v in dictionary.items():
            if k != "_id":
                setattr(self, k, v)


class sportModel:

    name = "Default"
    rating = 0.0

    def __init__(self, dictionary):
        for k, v in dictionary.items():
            if k != "_id":
                setattr(self, k, v)


class weatherSummaryModel:

    windInfo = {}
    waveInfo = {}
    climateInfo = {}

    def __init__(self, dictionary):
        for k, v in dictionary.items():
            if k != "_id":
                setattr(self, k, v)


class weatherEvalModel:

    windHigh = 0.0
    windLow = 0.0
    windAvg = 0.0
    windDirection = "Default"

    waveSize = 0.0
    wavePeriod = 0.0

    cloudCover = 0.0
    temperature = 0.0
    rain = 0.0

    def __init__(self, windHigh=None, windLow=None, windAvg=None, windDirection=None, waveSize=None, wavePeriod=None,
                 cloudCover=None, temperature=None, rain=None):
        self.windHigh = windHigh
        self.windLow = windLow
        self.windAvg = windAvg
        self.windDirection = windDirection

        self.waveSize = waveSize
        self.wavePeriod = wavePeriod

        self.cloudCover = cloudCover
        self.temperature = temperature
        self.rain = rain
