import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    MONGO_URL = os.getenv('WHATSGOOD_CONSTR')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    MONGO_URL = os.getenv('WHATSGOOD_CONSTR')


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    MONGO_URL = os.getenv('WHATSGOOD_CONSTR')


class ProductionConfig(Config):
    DEBUG = False

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.MONGO_URL

sports = [
    "Kiting",
    "Surfing",
    "Climbing"
]