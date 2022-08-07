from flask import Flask, redirect, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/participants.db'

# database setup
db = SQLAlchemy(app)

# creates Events table
class Events(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    event_name = db.Column(db.String(50), nullable=False)
    event_type = db.Column(db.String(20), nullable=False)
    date_created = db.Column( db.DateTime, default=datetime.utcnow)

    def __init__(self, event_name, event_type):
        self.event_name = event_name
        self.event_type = event_type

    def __repr__(self):
        return '<Task %r' % self.id

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
            return redirect('/')
        except:
            return 'There was an issue adding your task.'
    else:
        events = Events.query.order_by(Events.date_created).all()
        return render_template('add-events.html', events=events)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)