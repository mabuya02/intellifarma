from . import db
from datetime import datetime


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    First_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column('password', db.String(255), nullable=False)  
    email = db.Column(db.String(255), unique=True, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = db.relationship('Role', backref=db.backref('users', lazy=True))
    contact_number = db.Column(db.String(20))
    farm_location = db.Column(db.String(255))
    registration_date = db.Column(db.DateTime, server_default=db.func.now())
    status = db.Column(db.Enum('Active', 'Inactive'), server_default='Active')
    activation_code = db.Column(db.String(50)) 
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('sessions', lazy=True))
    session_token = db.Column(db.String(255), nullable=False)
    login_timestamp = db.Column(db.DateTime, nullable=False)
    logout_timestamp = db.Column(db.DateTime, nullable=True)


class SoilParameters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('soil_parameters', lazy=True))
    nitrogen_level = db.Column(db.Float)
    phosphorus_level = db.Column(db.Float)
    potassium_level = db.Column(db.Float)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    ph_level = db.Column(db.Float)
    rainfall = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    

class CropDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    crop_image = db.Column(db.String(255)) 
    prediction_id = db.Column(db.Integer, db.ForeignKey('crop_prediction.id'))
    prediction = db.relationship('CropPrediction', backref=db.backref('crop_details', lazy=True))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    

class CropPrediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parameter_id = db.Column(db.Integer, db.ForeignKey('soil_parameters.id'))
    parameters = db.relationship('SoilParameters', backref=db.backref('crop_prediction', lazy=True))
    predicted_crop_name = db.Column(db.String(50))
    prediction_date = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('reviews', lazy=True))
    prediction_id = db.Column(db.Integer, db.ForeignKey('crop_prediction.id'))
    prediction = db.relationship('CropPrediction', backref=db.backref('reviews', lazy=True))
    rating = db.Column(db.Integer)  
    review_text = db.Column(db.Text)
    review_date = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    
    