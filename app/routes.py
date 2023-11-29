
from datetime import datetime
from flask import Blueprint, jsonify,  request
from flask_restful import Api, Resource, marshal_with, fields
from app.db_operations import get_latest_soil_parameters_by_user
from app.models import CropPrediction, Review, Role, Session,  SoilParameters, User
from app import db
from uuid import uuid4
import bcrypt
from app.services import  generate_activation_code, predict_crop_for_user, send_activation_code_email, send_activation_email, user_verification_email, user_verification_successfull


main = Blueprint('main', __name__)
api = Api(main)
soil_parameters_bp = Blueprint('soil_parameters', __name__)
soil_parameters_api = Api(soil_parameters_bp)

user_review_bp = Blueprint('review', __name__)
user_review_api = Api(user_review_bp)

user_activation_bp = Blueprint ('user',__name__)
user_activation_api = Api(user_activation_bp)

logout_user_bp = Blueprint('session',__name__)
logout_user_api = Api(logout_user_bp)

all_reviews_bp = Blueprint('review',__name__)
all_reviews_api = Api(all_reviews_bp)

class UserLogin(Resource):
    def post(self):
        data = request.json
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return {'message': 'Email and password are required'}, 400
        
        status = "active"
        
        if not status:
            return{'message':'Account is not verified'},400

        user = User.query.filter_by(email=email).first()

        if not user or not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            return {'message': 'Invalid credentials'}, 401
        
        
        if user.status != 'Active':
            # User not verified, send verification email and return a message
            activation_code = send_activation_code_email(email)
            if activation_code:
                user_verification_email(email, activation_code)
                message = f'Your account has not been verified. Verification code sent to your email: {email}.'
                return {'message': message}, 400
            else:
                return {'message': 'Failed to send verification code'}, 500
            

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
    def post(self):
        data = request.json
        
        existing_user = User.query.filter_by(email=data.get('email')).first()
        

        role_id = 2
        role = Role.query.get(role_id)
        status = data.get('status') or 'inactive'

        if not role:
            return {'message': 'Role does not exist'}, 400
        
        hashed_password = bcrypt.hashpw(data.get('password').encode('utf-8'), bcrypt.gensalt())
        activation_code = generate_activation_code() 

        new_user = User(
            First_name=data.get('First_name'),
            last_name=data.get('last_name'),
            password=hashed_password.decode('utf-8'),
            email=data.get('email'),
            role=role,
            role_id=role_id,
            contact_number=data.get('contact_number'),
            farm_location=data.get('farm_location'),
            status=status,
            activation_code=activation_code        
        )
        if existing_user:
            return {'message': 'Email already exists'}, 400
        
        try:
            db.session.add(new_user)
            db.session.commit()
            send_activation_email(new_user.email, activation_code)
            return jsonify({'message': 'Registered successfully. Verification code has been sent to your email address'}), 201
        
        except Exception as e:
            db.session.rollback()
            return {'message': f'Failed to register user: {str(e)}'}, 500
main.add_url_rule('/register', view_func=RegisterUser.as_view('register_user'))

from flask import jsonify

class ActivateUserResource(Resource):
    def post(self):
        data = request.json
        email = data.get('email')
        activation_code = data.get('activation_code')

        user = User.query.filter_by(email=email, activation_code=activation_code).first()

        if user:
            user.status = 'Active'
            user.activation_code = 'verified'
            db.session.commit()
            user_verification_successfull(email)
            return jsonify({'message': 'User activated successfully'})
        else:
            return jsonify({'message': 'Invalid activation code or email'}), 400  

user_activation_api.add_resource(ActivateUserResource, '/activate')


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


#----------------------------------------------------------------------------------------------------------------------

class SoilParametersByUser(Resource):
    def get(self, user_id):
        latest_param = get_latest_soil_parameters_by_user(user_id)
        prediction =  predict_crop_for_user(user_id)
        if prediction is not None and len(prediction) > 0:
            crop_prediction = CropPrediction(
                parameter_id=latest_param.id,
                predicted_crop_name=str(prediction[0]),
                prediction_date=datetime.utcnow()
            )
            db.session.add(crop_prediction)
            db.session.commit()

            return jsonify({'prediction': prediction})  # Return the entire prediction list
        else:
            return jsonify({'message': 'Prediction failed '}), 404 
        
api.add_resource(SoilParametersByUser, '/soil-parameters/<int:user_id>')

#----------------------------------------------------------------------------------------------------------------------



user_review_fields ={
    'user_id': fields.Integer,
    'prediction_id':fields.Integer,
    'rating':fields.Integer,
    'review_text':fields.String,
    
}
class UserReviewResource(Resource):
    @marshal_with(user_review_fields)
    def post(self):
        data = request.json
        
        new_user_review = Review(
            user_id=data.get('user_id'),
            prediction_id=data.get('prediction_id'),
            rating=data.get('rating'),
            review_text=data.get('review_text')
          )
        
        try :
            db.session.add(new_user_review)
            db.session.commit()
            return new_user_review, 201
        except Exception as e :
            db.session.rollback()
            return{'message':f'Failed to store the user reviews: {str(e)}'},500
        
user_review_api.add_resource(UserReviewResource, '/user-reviews')

class AllReviews(Resource):
    def get(self):
        reviews = Review.query.all()
        review_list = []

        for review in reviews:
            review_info = {
                'user_name': review.user.First_name, 
                'rating': review.rating,
                'comment': review.review_text,
                'review_date': review.review_date.strftime("%Y-%m-%d %H:%M:%S")
            }
            review_list.append(review_info)

        return jsonify({'reviews': review_list})
    
all_reviews_api.add_resource(AllReviews, '/all-reviews')




class LogoutResource(Resource):
    def post(self, user_id):
        sessions = Session.query.filter_by(user_id=user_id).all()

        for session in sessions:
            session.logout_timestamp = datetime.now()

        db.session.commit()

        return {'message': 'Logged out successfully'}, 200
logout_user_api.add_resource(LogoutResource, '/logout/<int:user_id>')
    
        
