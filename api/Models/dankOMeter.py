#rating script

class dankOMeter():

    def getRating(self, sport, weatherObj):

        if (sport == "Kiting"):
            return self.getKitingRating(weatherObj)
        if (sport == "Surfing"):
            return self.getSurfingRating(weatherObj)
        if (sport == "Climbing"):
            return self.getClimbingRating(weatherObj)

    def getKitingRating(self, weatherObj):


        if weatherObj["latestWindReading"]['high'] >= 35:
            return 5
        elif weatherObj["latestWindReading"]['high'] >= 30:
            return 4.5
        elif weatherObj["latestWindReading"]['high'] >= 25:
            return 4
        elif weatherObj["latestWindReading"]['high'] >= 20:
            return 3
        elif weatherObj["latestWindReading"]['high'] >= 15:
            return 2
        elif weatherObj["latestWindReading"]['avg'] >= 10:
            return 1
        else: 
            return 0
        
    def getSurfingRating(self, weatherObj):
        return 1
    def getClimbingRating(self, weatherObj):
        return 1
