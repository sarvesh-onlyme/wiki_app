from flask import Flask

app = Flask(__name__)
from wiki_app import config
from wiki_app import views