from os import environ
from flask import Flask
from app.api import sport_bp, weather_bp, url_prefix
import pymongo

app = Flask(__name__)
app.config.from_object(environ.get('WHATSGOOOD_ENV'))

# Initialize Flask Mongo DB
client = pymongo.MongoClient(app.config['MONGO_URL'])
db = client[app.config['DB_NAME']]

# Register blue prints
app.register_blueprint(sport_bp, url_prefix=url_prefix)
app.register_blueprint(weather_bp, url_prefix=url_prefix)
