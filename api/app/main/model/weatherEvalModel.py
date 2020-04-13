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

    def __init__(self, windHigh = None , windLow = None , windAvg = None , windDirection = None , waveSize = None , wavePeriod = None , cloudCover = None , temparature = None , chanceOfRain = None ):
        self.windHigh = windHigh
        self.windLow = windLow
        self.windAvg = windAvg
        self.windDirection = windDirection

        self.waveSize = waveSize
        self.wavePeriod = wavePeriod

        self.cloudCover = cloudCover
        self.temparature = temparature
        self.chanceOfRain = chanceOfRain