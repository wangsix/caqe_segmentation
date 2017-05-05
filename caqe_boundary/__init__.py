from flask import Flask
from flask_bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask('caqe_boundary')

Bootstrap(app)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://wangsix:Six0420!@localhost/segmentation_beatles"

