from app.error import incompleteWeightError

# region Documentation

# Weighting Model Docs:

# All weights must add up to 1

# In the case that a rating should get better as a particular piece of weather info tends toward a certain value
# eg. Temparature for kiting can never really be too high.
# Simply give it a weight in the sportWeight table, and it will be normalised between a max and min value using the
# normalise table

# If there is an optimal point for a particular piece of weather info(eg. climbing where you'd like temps to be around
# 10-15 deg)
# Then you have to pass in a dictionary, eg.

# "temparature": {
#     "weight": .40,
#     "optimalValue" : 15,
#     "tolerance" : 5
# }
#
# Where optmialValue = the value that would yield the best results for that sport
# And tolerance is how far to either side you are willing to accept. Note that this is exclusive.
# If your optimal is 10 and your tolerance is 5, 15 will yield a 0 rating.

# If you need to use an optimal value, but your tolerance is lower on one side than the other, then you can set
# upperBound and lowerBound:

# "temparature": {
#     "weight": .40,
#     "optimalValue" : 15,
#     "upperBound": 20,
#     "lowerBound": 12
# }

# Currently values increase linearly as they tend toward your optimal value

# eg. :

#                                    dankness (y)
#                                       |
#                                      10------------- 0
#                                       |             / \
#                                       |           /    \
#                                       |         /       \
#                                       |       /          \         upperBound
#                                       |     /             \      /
#                                       |   /                \   /
# -----------------------------------------1-------------6-----8--------------------- temp (x)
#                                       |  \            \
#                                       |   \            \
#                                       |    lowerBound   optimalValue
#                                       |
#                                       |
#                                       |
#
#
# endregion

# region Weights

sportWeights = {
    "ClimbingWeights": {
        "temparature": {
            "weight": .30,
            "optimalValue": 15,
            "tupperBound": 26,
            "lowerBound": 7
        },
        "windHigh": -.05,
        "windAvg": -.05,

        "cloudCover": -.10,
        "chanceOfRain": {
            "weight": .50,
            "optimalValue": 0,
            "upperBound": 25,
            "lowerBound": -1
        }
    },
    "SurfingWeights": {
        "windAvg": -.2,

        "waveSize": {
            "weight": .4,
            "optimalValue": 8,
            "upperBound": 20,
            "lowerBound": 2
        },
        "wavePeriod": -.1,

        "cloudCover": -.05,
        "temparature": .10,
        "chanceOfRain": -.15
    },
    "KitingWeights": {
        "windHigh": {
            "weight": .4,
            "optimalValue": 45,
            "upperBound": 70,
            "lowerBound": 7

        },
        "windAvg": {
            "weight": .3,
            "optimalValue": 35,
            "upperBound": 70,
            "lowerBound": 7

        },
        "waveSize": .1,
        "temparature": .1,
        "chanceOfRain": -.1
    }
}

normaliseTable = {
    "wind": {
        "max": 30.0,
        "min": 5.0,
    },
    "windDirection": {
        "SE": .5,
        "SSE": .5,
        "NW": .3,
        "SW": .2
    },
    "waveSize": {
        "max": 10.0,
        "min": 2.0
    },
    "wavePeriod": {
        "max": 17.0,
        "min": 7.0
    },
    "temparature": {
        "max": 50.0,
        "min": 0.0
    }
}

# endregion

# TODO: create an optimal plateau lower and upper bound, end of plateau bound
# should then taper down to actual lower and upper bounds
def weight(weatherModel, sport):

    rating = 0.0

    weightName = sport + "Weights"

    sportWeightModel = sportWeights[weightName]

    totalWeight = 0.0

    for key in sportWeightModel:

        if isinstance(sportWeightModel[key], dict):

            value = normaliseForOptimal(
                sportWeightModel[key], weatherModel[key])
            weight = sportWeightModel[key]['weight']

        else:
            value = normalise(key, weatherModel[key])
            weight = sportWeightModel[key]

        rating += value * weight
        totalWeight += abs(weight)

    if round(totalWeight, 3) != 1:
        raise incompleteWeightError(totalWeight)

    return rating


def normalise(key, value):

    normalisedValue = 0.0

    if key == "windDirection":
        try:
            normalisedValue = normaliseTable["windDirection"][value]
        except(KeyError):
            normalisedValue = 0.0

    if "wind" in key:
        maxVal = normaliseTable["wind"]['max']
        minVal = normaliseTable["wind"]['min']
    else:
        try:
            maxVal = normaliseTable[key]['max']
            minVal = normaliseTable[key]['min']
        except(KeyError):
            return value
            # No value found in normalise table,
            # either not nessesary to normalise or not yet supported

    calculatedTotal = maxVal - minVal

    normalisedValue = (value - minVal) / calculatedTotal

    if normalisedValue > 1:
        normalisedValue = 1
    if normalisedValue < 0:
        normalisedValue = 0

    return normalisedValue


def normaliseForOptimal(sportWeight, value):

    normalisedValue = 0.0

    optimalValue = sportWeight['optimalValue']

    if "tolerance" in sportWeight:

        tolerance = sportWeight['tolerance']

        difference = abs(optimalValue - value)

        percentLoss = difference / tolerance

        normalisedValue = 1 - percentLoss

    elif "upperBound" in sportWeight and "lowerBound" in sportWeight:

        diff = value - optimalValue
        diffAbs = abs(value - optimalValue)

        if diff < 0:
            tolerance = optimalValue - sportWeight["lowerBound"]
        elif diff > 0:
            tolerance = sportWeight["upperBound"] - optimalValue
        elif diff == 0:
            return 1

        percentLoss = diffAbs / tolerance
        normalisedValue = 1 - percentLoss

    if normalisedValue > 1:
        normalisedValue = 1
    if normalisedValue < 0:
        normalisedValue = 0

    return normalisedValue
