

from caqe_boundary import db
from caqe_boundary import app

song_annotator = db.Table('song_annotator',
    db.Column('song_id', db.Integer, db.ForeignKey('song.id')),
    db.Column('annotator_id', db.Integer, db.ForeignKey('annotator.id'))
)


class Song(db.Model):
    __tablename__ = 'song'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    dataset = db.Column(db.String(16), default='beatles')
    max_idx = db.Column(db.Integer)

    annotators = db.relationship('Annotator',
                                 secondary=song_annotator,
                                 backref=db.backref('song', lazy='dynamic')
                                 )

    annotations = db.relationship('Annotation', backref='song', lazy='dynamic')

    def __init__(self, name, dataset, max_id):
        self.name = name
        self.dataset = dataset
        self.max_idx = max_id

    def __repr__(self):
        return "<Song id=%r, name=%r, dataset=%r>" % (self.id, self.name, self.dataset)

    def get_annotations_by_annotator(self, annotator_id):
        pass


class Annotator(db.Model):
    __tablename__ = 'annotator'

    id = db.Column(db.Integer, primary_key=True)
    crowd_worker_id = db.Column(db.String(256), unique=True)
    status = db.Column(db.Boolean, default=True)
    gender = db.Column(db.String(6), default='male')
    age = db.Column(db.Integer, default=18)
    musician = db.Column(db.Boolean, default=False)
    country = db.Column(db.String(16), default='USA')
    music_hour = db.Column(db.String(32))
    instrument = db.Column(db.Text)

    songs = db.relationship('Song',
                            secondary=song_annotator,
                            backref=db.backref('annotator', lazy='dynamic'))

    annotations = db.relationship('Annotation', backref='annotator', lazy='dynamic')

    def __init__(self, crowd_worker_id, status, gender, age, musician, country, music_hours, instrument):
        self.crowd_worker_id = crowd_worker_id
        self.status = status
        self.gender = gender
        self.age = age
        self.musician = musician
        self.country = country
        self.music_hour = music_hours
        self.instrument = instrument

    def __repr__(self):
        return "<Annotator id=%r, musician=%r, crowd_worker_id=%r>" % (self.id, self.musician, self.crowd_worker_id)


class Annotation(db.Model):
    __tablename__ = 'annotation'

    id = db.Column(db.Integer, primary_key=True)
    annotator_id = db.Column(db.Integer, db.ForeignKey('annotator.id'))
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'))
    boundary_time = db.Column(db.Float)
    clip_id = db.Column(db.Integer)
    agree_prob = db.Column(db.Float)

    def __init__(self, annotator_id, song_id, time, idx):
        self.annotator_id = annotator_id
        self.song_id = song_id
        self.boundary_time = time
        self.clip_id = idx

    def __repr__(self):
        return "<Annotation id=%r, Song id=%r, Annotator id=%r, Time=%r>" % \
               (self.id, self.song_id, self.annotator_id, self.boundary_time)
