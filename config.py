import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    MONGO_URL = os.environ.get('WHATSGOOOD_CONSTR')
    DB_NAME = 'plagiarismDB'
    DEVELOPMENT = False
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SPORTS = [
        "kiting",
        "surfing",
        "climbing",
        "cycling"
    ]
    FORECASTHOURS = [
        10, 12, 14, 16, 18, 20
    ]


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    ENV = "development"


class TestingConfig(Config):
    TESTING = True
    ENV = "development"


class ProductionConfig(Config):
    DEBUG = False
    ENV = "production"
