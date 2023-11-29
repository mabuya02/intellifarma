from flask_mail import Message
import joblib
import numpy as np
from app import mail
import random
import string
from app.db_operations import get_latest_soil_parameters_by_user


def generate_activation_code(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def send_activation_email(email, activation_code):
    msg = Message('Activate your Intellifarma Account', sender='noreply@intellifarma.com', recipients=[email])
    msg.body = f'Your activation code is: {activation_code}. Use this code to activate your account.'
    mail.send(msg)

def send_activation_code_email(email):
    activation_code = generate_activation_code()
    try:
        send_activation_email(email, activation_code)
        return activation_code
    except Exception as e:
        return None
    
    
def user_verification_email(email, activation_code):
    msg = Message('Activate your Intellifarma Account', sender='noreply@intellifarma.com', recipients=[email])
    msg.body = f' Your tried logging in but you account has not been verfied. \n Kindly activate your account to login. Your activation code is: {activation_code}. Use this code to activate your account.'
    mail.send(msg)
    
def user_verification_successfull(email,First_name):
    msg = Message('Verification successfull', sender='noreply@intellifarma.com', recipients=[email])
    msg.body = f'Hello {First_name},Welcome to Intellifarma! Your account has been successfully verified. '
    mail.send(msg)

model = joblib.load('ml_model/smart_farmingmodel.joblib')
def predict_crop_for_user(user_id):
    latest_params = get_latest_soil_parameters_by_user(user_id)
    if latest_params:
        features = [
                latest_params.nitrogen_level,
                latest_params.phosphorus_level,
                latest_params.potassium_level,
                latest_params.temperature,
                latest_params.humidity,
                latest_params.ph_level,
                latest_params.rainfall
            ]
        
    features_array = np.array(features).reshape(1, -1) 
    
    prediction = model.predict(features_array)
    
    return prediction.tolist() if prediction is not None else None  # Convert prediction to list

    
    



