from src.main import app
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
db.init_app(app)

# creates Events table
class Events(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    event_name = db.Column(db.String(50), nullable=False)
    event_type = db.Column(db.String(20), nullable=False)
    date_created = db.Column( db.DateTime, default=datetime.utcnow)

    def __init__(self, event_name, event_type):
        self.event_name = event_name
        self.event_type = event_type

class Teams(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    team_name = db.Column(db.String(50), nullable=True)
    event_1 = db.Column(db.String(50), nullable=True)
    event_2 = db.Column(db.String(50), nullable=True)
    event_3 = db.Column(db.String(50), nullable=True)
    event_4 = db.Column(db.String(50), nullable=True)
    event_5 = db.Column(db.String(50), nullable=True)
    date_added = db.Column( db.DateTime, default=datetime.utcnow)

    def __init__(self, team_name, event_1, event_2, event_3, event_4, event_5):
        self.team_name = team_name
        self.event_1 = event_1
        self.event_2 = event_2
        self.event_3 = event_3
        self.event_4 = event_4
        self.event_5 = event_5

class TeamMembers(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    member_1 = db.Column(db.String(50), nullable=False)
    member_2 = db.Column(db.String(50), nullable=False)
    member_3 = db.Column(db.String(50), nullable=False)
    member_4 = db.Column(db.String(50), nullable=False)
    member_5 = db.Column(db.String(50), nullable=False)
    team_name = db.Column(db.Integer, db.ForeignKey('teams.id'))

    def __init__(self, member_1, member_2, member_3, member_4, member_5):
        self.member_1 = member_1
        self.member_2 = member_2
        self.member_3 = member_3
        self.member_4 = member_4
        self.member_5 = member_5

class Individuals(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    individual_name = db.Column(db.String(50), nullable=True)
    event_1 = db.Column(db.String(50), nullable=True)
    event_2 = db.Column(db.String(50), nullable=True)
    event_3 = db.Column(db.String(50), nullable=True)
    event_4 = db.Column(db.String(50), nullable=True)
    event_5 = db.Column(db.String(50), nullable=True)
    date_added = db.Column( db.DateTime, default=datetime.utcnow)

    def __init__(self, individual_name, event_1, event_2, event_3, event_4, event_5):
        self.individual_name = individual_name
        self.event_1 = event_1
        self.event_2 = event_2
        self.event_3 = event_3
        self.event_4 = event_4
        self.event_5 = event_5

class TeamScores(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    individual = db.Column(db.String(50), nullable=False)
    event_name = db.Column(db.String(50), nullable=False)
    rank = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    date_added = db.Column( db.DateTime, default=datetime.utcnow)

    def __init__(self, individual, event_name, rank, score):
        self.individual = individual
        self.event_name = event_name
        self.rank = rank
        self.score = score

class IndividualScores(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    individual = db.Column(db.String(50), nullable=False)
    event_name = db.Column(db.String(50), nullable=False)
    rank = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    date_added = db.Column( db.DateTime, default=datetime.utcnow)

    def __init__(self, individual, event_name, rank, score):
        self.individual = individual
        self.event_name = event_name
        self.rank = rank
        self.score = score