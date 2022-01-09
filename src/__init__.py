from flask import Flask

app = Flask(__name__)

from src import route
from src import errorHandlers