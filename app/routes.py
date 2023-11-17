import datetime
from flask import Blueprint, request
from flask_restful import Api, Resource, marshal_with, fields , reqparse
from app.models import Role, SoilParameters, User
from app import db
from werkzeug.security import check_password_hash


main = Blueprint('main', __name__)
api = Api(main)
soil_parameters_bp = Blueprint('soil_parameters', __name__)
soil_parameters_api = Api(soil_parameters_bp)



# --------------------------------------------------User registration-----------------------------------------------------------
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
        

        if not role:
            return {'message': 'Role does not exist'}, 400

        new_user = User(
            First_name=data.get('First_name'),
            last_name=data.get('last_name'),
            password=data.get('password'),
            email=data.get('email'),
            role=role,
            role_id=role_id,  
            contact_number=data.get('contact_number'),
            farm_location=data.get('farm_location'),
            status=data.get('status', 'Active')  # Default status to 'Active' if not provided( user verification using email)
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



# --------------------------------------------------Soil parameters-----------------------------------------------------------

soil_parameters_fields = {
    'id': fields.Integer,
    'user_id': fields.Integer,
    'nitrogen_level': fields.Float,
    'phosphorus_level': fields.Float,
    'potassium_level': fields.Float,
    'temperature': fields.Float,
    'humidity': fields.Float,
    'ph_level': fields.Float,
    'rainfall': fields.Float,
}

class SoilParametersResources(Resource):
    @marshal_with(soil_parameters_fields)
    def post(self):
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
        
        try:
            db.session.add(new_soil_parameter)
            db.session.commit()
            return new_soil_parameter, 201 
        except Exception as e:
            db.session.rollback()
            return {'message': f'Failed to store the soil parameters: {str(e)}'}, 500

soil_parameters_api.add_url_rule('/soil_parameters', view_func=SoilParametersResources.as_view('soil_parameters'))
