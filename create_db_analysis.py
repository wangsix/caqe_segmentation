

import caqe_boundary.process as process

import caqe_boundary
from caqe_boundary import db, app

if app.config['SQLALCHEMY_BINDS']:
    db.drop_all(bind=app.config['SQLALCHEMY_BINDS'])
    db.create_all(bind=app.config['SQLALCHEMY_BINDS'])
else:
    print "No Binds specified."

with caqe_boundary.app.app_context():
    process.insert_data()