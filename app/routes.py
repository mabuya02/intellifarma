
from datetime import datetime
from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource, marshal_with, fields
from app.models import Role, Session,  SoilParameters, User
from app import db
from uuid import uuid4
import bcrypt



main = Blueprint('main', __name__)
api = Api(main)
soil_parameters_bp = Blueprint('soil_parameters', __name__)
soil_parameters_api = Api(soil_parameters_bp)


class UserLogin(Resource):
    def post(self):
        data = request.json
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return {'message': 'Email and password are required'}, 400

        user = User.query.filter_by(email=email).first()

        if not user or not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            return {'message': 'Invalid credentials'}, 401
        
                # Generate a session token
        session_token = str(uuid4())

        # Create a session for the user
        new_session = Session(
            user_id=user.id,
            session_token=session_token,
            login_timestamp=datetime.utcnow()
        )
        
        try:
            db.session.add(new_session)
            db.session.commit()
            return {
                'message': 'Login successful',
                'session_token': session_token
            }, 200
        except Exception as e:
            db.session.rollback()
            return {'message': f'Failed to create session: {str(e)}'}, 500


# Add the login route to the main Blueprint
main.add_url_rule('/login', view_func=UserLogin.as_view('user_login'))

user_fields = {
    'id': fields.Integer,
    'First_name': fields.String,
    'last_name': fields.String,
    'password': fields.String,
    'email': fields.String,
    'role_id': fields.Integer,
    'contact_number': fields.String,
    'farm_location': fields.String,
    'status': fields.String,
}


class RegisterUser(Resource):
    @marshal_with(user_fields)  # Marshal the output with the defined fields
    def post(self):
        data = request.json

        role_id = 2
        role = Role.query.get(role_id)
        status = data.get('status') or 'Active'

        if not role:
            return {'message': 'Role does not exist'}, 400
        
        hashed_password = bcrypt.hashpw(data.get('password').encode('utf-8'), bcrypt.gensalt())

        new_user = User(
            First_name=data.get('First_name'),
            last_name=data.get('last_name'),
            password=hashed_password.decode('utf-8'),
            email=data.get('email'),
            role=role,
            role_id=role_id,
            contact_number=data.get('contact_number'),
            farm_location=data.get('farm_location'),
            status=status
            
        )

        try:
            db.session.add(new_user)
            db.session.commit()
            return new_user, 201  # Return the newly created user
        except Exception as e:
            db.session.rollback()
            return {'message': f'Failed to register user: {str(e)}'}, 500


# Add the routes to the blueprint
main.add_url_rule('/register', view_func=RegisterUser.as_view('register_user'))

soil_parameters_fields = {
    'id' : fields.Integer,
    'user_id' : fields.Integer,
    'nitrogen_level' : fields.Float,
    'phosphorus_level' : fields.Float,
    'potassium_level' : fields.Float,
    'temperature' : fields.Float,
    'humidity' : fields.Float,
    'ph_level' : fields.Float,
    'rainfall' : fields.Float,
}


class SoilParametersResources(Resource) :
    @marshal_with(soil_parameters_fields)
    def post(self) :
        data = request.json

        new_soil_parameter = SoilParameters(
            user_id=data.get('user_id'),
            nitrogen_level=data.get('nitrogen_level'),
            phosphorus_level=data.get('phosphorus_level'),
            potassium_level=data.get('potassium_level'),
            temperature=data.get('temperature'),
            humidity=data.get('humidity'),
            ph_level=data.get('ph_level'),
            rainfall=data.get('rainfall'),
        )

        try :
            db.session.add(new_soil_parameter)
            db.session.commit()
            return new_soil_parameter, 201
        except Exception as e :
            db.session.rollback()
            return {'message' : f'Failed to store the soil parameters: {str(e)}'}, 500
        
soil_parameters_api.add_resource(SoilParametersResources, '/soil-parameters')






