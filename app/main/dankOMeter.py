# #rating script
class dankOMeter():

    def getRating(self, sport, weatherEvalModel):

        if (sport == "Kiting"):
            return self.getKitingRating(weatherEvalModel)
        if (sport == "Surfing"):
            return self.getSurfingRating(weatherEvalModel)
        if (sport == "Climbing"):
            return self.getClimbingRating(weatherEvalModel)

    def getKitingRating(self, weatherEvalModel):

        if weatherEvalModel.windHigh >= 35:
            return 5
        elif weatherEvalModel.windHigh >= 30:
            return 4.5
        elif weatherEvalModel.windHigh >= 25:
            return 4
        elif weatherEvalModel.windHigh >= 20:
            return 3
        elif weatherEvalModel.windHigh >= 15:
            return 2
        elif weatherEvalModel.windAvg >= 10:
            return 1
        else: 
            return 0
        
    def getSurfingRating(self, weatherEvalModel):
        return 1
    def getClimbingRating(self, weatherEvalModel):
        return 1
