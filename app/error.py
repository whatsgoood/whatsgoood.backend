class incompleteWeightError(Exception):

    message = "Weights did not add up to 1"

    def __init__(self, sport=None):
        if sport is not None:
            message = f"Weights for {sport} did not add up to 1"

class NormaliseKeyNotFoundError(Exception):

    message = "No matching key was found in the normalise table"

    def __init__(self, key=None):
        if key is not None:
            message = f"Key '{key}' was found in the normalise table"
