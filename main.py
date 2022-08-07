from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime
from src.models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/participants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add-events', methods=['POST', 'GET'])
def add_events():
    if request.method == 'POST':
        event_name = request.form['event-name']
        event_type = request.form['event-type']
        new_event = Events(event_name, event_type)

        try:    
            db.session.add(new_event)
            db.session.commit()
            return redirect('/add-events')
        except:
            return 'There was an issue adding your task.'
    else:
        events = Events.query.order_by(Events.date_created).all()
        return render_template('add-events.html', events=events)

@app.route('/add-participants', methods=['POST', 'GET'])
def add_participants():
    if request.method == 'POST':
        participant_name = request.form['participant-name']
        event_type = request.form['event-type']
        member_1 = request.form['member-1']
        member_2 = request.form['member-2']
        member_3 = request.form['member-3']
        member_4 = request.form['member-4']
        member_5 = request.form['member-5']
        event_1 = request.form['event-1']
        event_2 = request.form['event-2']
        event_3 = request.form['event-3']
        event_4 = request.form['event-4']
        event_5 = request.form['event-5']
        if event_type == 'team':
        
            team = Teams(participant_name, event_1, event_2, event_3, event_4, event_5)
            team_members = TeamMembers(member_1, member_2, member_3, member_4, member_5)

            try:
                db.session.add(team)
                db.session.add(team_members)
                db.session.commit()
                return redirect('/add-participants')
            except:
                return 'There was an issue adding your participant.'

        elif event_type == "individual":
            individual = Individuals(participant_name, event_1, event_2, event_3, event_4, event_5)

            try:
                db.session.add(individual)
                db.session.commit()
                return redirect('/add-participants')
            except:
                return 'There was an issue adding your participant.'
    else:
        events = Events.query.order_by(Events.event_name).all()
        return render_template('add-participants.html', events=events)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)