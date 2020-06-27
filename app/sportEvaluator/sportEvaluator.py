from app.sportEvaluator.error import incompleteWeightError, NormaliseKeyNotFoundError
from app.sportEvaluator.evalConfig import normaliseTable, ratingPhrases, sportWeights
import math

# region Documentation

# Weighting Model Docs:

# All weights must add up to 1

# In the case that a rating should get better as a particular piece of weather info tends toward a certain value
# eg. temperature for kiting can never really be too high.
# Simply give it a weight in the sportWeight table, and it will be normalised between a max and min value using the
# normalise table

# If there is an optimal point for a particular piece of weather info(eg. climbing where you'd like temps to be around
# 10-15 deg)
# Then you have to pass in a dictionary, eg.

# "temperature": {
#     "weight": .40,
#     "optimalValue" : 15,
#     "tolerance" : 5
# }
#
# Where optimalValue = the value that would yield the best results for that sport
# And tolerance is how far to either side you are willing to accept. Note that this is exclusive.
# If your optimal is 10 and your tolerance is 5, 15 will yield a 0 rating.

# If you need to use an optimal value, but your tolerance is lower on one side than the other, then you can set
# upperBound and lowerBound:

# "temperature": {
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

def getRatingModel(weatherModel, sport):

    outputModel = {
        "name": sport.title(),
        "rating": 0.0
    }

    rating = 0.0

    weightName = sport + "Weights"

    sportWeightModel = sportWeights[weightName]

    outputModel['context'] = initaliseContextModel(sport)

    for key in sportWeightModel:

        if isinstance(sportWeightModel[key], dict):

            value = normaliseForOptimal(
                sportWeightModel[key], weatherModel[key])
            weight = sportWeightModel[key]['weight']

        else:

            weight = sportWeightModel[key]

            value = normalise(key, weatherModel[key])

        ratingIdv = value * weight

        outputModel['rating'] += ratingIdv
        outputModel = getContext(outputModel, key, sport, ratingIdv, value, weatherModel[key], weight)

    if outputModel['rating'] < 0:
        outputModel['rating'] = 0

    return outputModel


def normalise(key, value):

    normalisedValue = 0.0

    if key == "windDirection":
        try:
            normalisedValue = normaliseTable["windDirection"][value]
        except(KeyError):
            normalisedValue = 0.0
    else:
        try:
            maxVal = normaliseTable[key]['max']
            minVal = normaliseTable[key]['min']
        except(KeyError):
            return value

    calculatedTotal = maxVal - minVal

    normalisedValue = (value - minVal) / calculatedTotal

    if normalisedValue > 1:
        normalisedValue = 1
    if normalisedValue < 0:
        normalisedValue = 0

    return normalisedValue


def normaliseForOptimal(sportWeight, value):

    normalisedValue = 0.0

    if "tolerance" in sportWeight:

        optimalValue = sportWeight['optimalValue']

        tolerance = sportWeight['tolerance']

        difference = abs(optimalValue - value)

        percentLoss = difference / tolerance

        normalisedValue = 1 - percentLoss

    elif "optimalUpperBound" in sportWeight and "optimalLowerBound" in sportWeight:

        if value <= sportWeight['optimalUpperBound'] and value >= sportWeight['optimalLowerBound']:

            return 1

        elif value > sportWeight['optimalUpperBound']:
            diff = value - sportWeight['optimalUpperBound']
            tolerance = sportWeight["upperBound"] - sportWeight['optimalUpperBound']

            if diff > tolerance:
                return 0

        elif value < sportWeight['optimalLowerBound']:
            diff = sportWeight['optimalLowerBound'] - value
            tolerance = sportWeight['optimalLowerBound'] - sportWeight["lowerBound"]

            if diff > tolerance:
                return 0

        percentLoss = diff / tolerance
        normalisedValue = 1 - percentLoss

    elif "upperBound" in sportWeight and "lowerBound" in sportWeight:

        optimalValue = sportWeight['optimalValue']

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

def initaliseContextModel(sport):

    try:
        summary = ratingPhrases[sport]['summary']
    except KeyError:
        summary = "No Summary"

    return {
        "summary": summary,
        "idvRatings": {}
    }

def getContext(ratingModel, key, sport, ratingIdv, normalisedVal, actualVal, weight):
    ratingModel['context']['idvRatings'][key] = {
        "ratingWeighted": ratingIdv,
        "ratingNormalised": normalisedVal,
        "value": actualVal,
        "Description": getRatingPhrase(key, normalisedVal, sport, weight)
    }
    return ratingModel

def getRatingPhrase(key, value, sport, weight):

    floored = math.floor(value / 0.33)

    if floored > 2:
        floored = 2
    if floored < 0:
        floored = 0

    if weight < 0:
        floored = abs(floored - 2)

    try:
        keyPhrase = ratingPhrases[sport][key][floored]
    except KeyError:
        return "No context"

    return keyPhrase
