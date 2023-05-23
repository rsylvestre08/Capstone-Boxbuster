from flask_bcrypt import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    state = db.Column(db.String(80), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    club_level = db.Column(db.String(255), nullable=False)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return self.username

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(255), nullable=False)
    model = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer)
    # Adds user_id as an Integer column on the car table which references the id column on user table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # Establishes object relation between car-user so we can grab values like car.user.username
    user = db.relationship("User")

# TODO: Add your models below, remember to add a new migration and upgrade database

class Administrator(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=True, nullable=False)

class Clublevel(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    platinum = db.Column(db.String(255), nullable=False)
    gold = db.Column(db.String(255), nullable=False)
    silver = db.Column(db.String(255), nullable=False)
    bronze = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float)
    user = db.relationship('user')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class MypaymentHistory(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    total_owed = db.Column(db.Float)
    billing_cycle = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

class Survey(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    genre_preference = db.Column(db.String(255), nullable=False)
    Budget = db.Column(db.Float)
    nationality = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


