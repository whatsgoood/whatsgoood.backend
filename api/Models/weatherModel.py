import json
from json import JSONEncoder

class weatherModel():

    avg = 0
    low = 0
    high = 0
    direction = ""

    def __init__(self, _avg, _low, _high, _dir):
        self.avg = _avg
        self.low = _low
        self.high = _high
        self.direction = _dir



