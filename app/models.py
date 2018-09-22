from datetime import datetime
import time
from app import db


class User(db.Model):
    zid = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.VARCHAR(255), index=True)
    last_name = db.Column(db.VARCHAR(255), index=True)
    person_type = db.Column(db.VARCHAR(255), index=True)
    phone_number = db.Column(db.Integer, index=True)
    email = db.Column(db.VARCHAR(255))
    password_hash = db.Column(db.String(128))
    photo_url = db.Column(db.String(128))
    available = db.Column(db.Boolean)
    location = db.Column(db.VARCHAR(255))


class Student(db.Model):
    zid = db.Column(db.Integer, db.ForeignKey('user.zid'), primary_key=True)
    degree = db.Column(db.VARCHAR(255))
    enrolled_courses = db.Column(db.VARCHAR(255))
    societies = db.Column(db.VARCHAR(255))


class Interests(db.Model):
    zid = db.Column(db.Integer, db.ForeignKey('user.zid'), primary_key=True)
    study_time = db.Column(db.BIGINT, index=True)
    study_length = db.Column(db.Integer)
    serious = db.Column(db.Boolean)
    sports = db.Column(db.VARCHAR(255))
    gaming = db.Column(db.VARCHAR(255))


class Matcher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    zid_src = db.Column(db.Integer, db.ForeignKey('user.zid'))
    zid_dest = db.Column(db.Integer, db.ForeignKey('user.zid'))
    match_time = db.Column(db.BIGINT, default=time.time())
    active = db.Column(db.Boolean)
    swiped_right = db.Column(db.Boolean, default=False)

#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#     password_hash = db.Column(db.String(128))
#
#     def __repr__(self):
#         return '<User {}>'.format(self.username)
#
#
# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.String(140))
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#     def __repr__(self):
#         return '<Post {}>'.format(self.body)
