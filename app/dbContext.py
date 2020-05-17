class dbContext:

    windCol = []
    waveCol = []
    weatherCol = []

    def __init__(self, _db):
        db = _db

        self.windCol = db['windCollection']
        self.waveCol = db['wavesCollection']
        self.weatherCol = db['weatherCollection']
