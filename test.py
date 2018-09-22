from flask import Flask, g
import sqlite3

app = Flask(__name__)
# from app import views

DATABASE = 'example.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def init_db():
    with app.app_context():
        db = get_db()
        db.commit()

@app.route('/')
def hello_world():
    init_db()
    return 'Hello World! DB init..'

@app.route('/places/<place>')
def inPlace(place):
    return 'Now you are in %s.' % place

 
if __name__ == '__main__':
    app.run()
    
