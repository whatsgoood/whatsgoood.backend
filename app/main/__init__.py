from flask import Flask
from .config import config_by_name
from .dbContext import dbContext
from .service import weatherService
# from .sportEvaluator import weight

weatherService = weatherService()

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_by_name[config_name])

    return app