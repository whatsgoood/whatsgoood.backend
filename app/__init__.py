from os import environ
from flask import Flask
import pymongo

app = Flask(__name__)
app_settings = environ.get('WHATSGOOOD_ENV')
app.config.from_object(app_settings)

# Initialize Flask Mongo DB
client = pymongo.MongoClient(app.config['MONGO_URL'])
db = client['plagiarismDB']

# Register blue prints
from app.api import rating_bp, weather_bp, url_prefix
app.register_blueprint(rating_bp, url_prefix=url_prefix)
app.register_blueprint(weather_bp, url_prefix=url_prefix)
