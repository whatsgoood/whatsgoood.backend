import os

from app.main import create_app
from .main.controller import weatherController

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
