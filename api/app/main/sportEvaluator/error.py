class incompleteWeightError(Exception):

    message = "Weights did not add up to 1"

    def __init__(self, sport = None):
        if sport != None:
            message = f"Weights for {sport} did not add up to 1"


    
