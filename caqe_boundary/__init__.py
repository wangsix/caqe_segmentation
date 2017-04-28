# from ..models import Participant
import logging
from flask import Flask
import os
from flask_bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.contrib.fixers import ProxyFix

app = Flask('caqe_boundary')

Bootstrap(app)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://wangsix:Six0420!@localhost/segmentation_beatles"
