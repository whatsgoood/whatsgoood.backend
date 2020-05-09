from json import JSONEncoder

class jsonEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__    
