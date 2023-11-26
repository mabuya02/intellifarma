from flask_mail import Message

from app import mail
import random
import string


from app.models import Session

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
    msg.body = f' Your tried logging in but you account has not been verfied. Kindly activate your account to login. Your activation code is: {activation_code}. Use this code to activate your account.'
    mail.send(msg)
    
def user_verification_successfull(email,First_name):
    msg = Message('Verification successfull', sender='noreply@intellifarma.com', recipients=[email])
    msg.body = f'Hello {First_name}, \n  Welcome to Intellifarma! Your account has been successfully verified. '
    mail.send(msg)
    
    
# def predict_crop_for_user(serialized_data):
#     data = {
#         'nitrogen_level': [serialized_data['nitrogen_level']],
#         'phosphorus_level': [serialized_data['phosphorus_level']],
#         'potassium_level': [serialized_data['potassium_level']],
#         'temperature': [serialized_data['temperature']],
#         'humidity': [serialized_data['humidity']],
#         'ph_level': [serialized_data['ph_level']],
#         'rainfall': [serialized_data['rainfall']]
#     }
#     prepared_data = pd.DataFrame(data)
    
#     return prepared_data 
    
    



