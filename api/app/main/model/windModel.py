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