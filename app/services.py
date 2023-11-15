from app import db, mail
from app.models import CropDetails, CropPrediction, Session, SoilParameters, User, Role
from werkzeug.security import generate_password_hash
from datetime import datetime
import pyotp
from flask_mail import Message
from werkzeug.security import check_password_hash
def send_email(subject, recipient, body):
    msg = Message(subject, recipients=[recipient])
    msg.body = body
    mail.send(msg)
    

def login_user(username, password):
    # Find the user by username
    user = User.query.filter_by(username=username).first()

    if user:
        # Check the password
        if check_password_hash(user.password, password):
            # Create a new session
            new_session = Session(user=user)
            db.session.add(new_session)
            db.session.commit()

            # Return the authenticated user and session
            return user, new_session

    # If no user is found or password is incorrect, raise an error
    raise ValueError('Invalid username or password.')

def register_user(username, password, email, enable_2fa=False, role_name='farmer', **kwargs):
    # Check if the role already exists or create a new one
    role = Role.query.filter_by(role_name=role_name).first()
    if not role:
        role = Role(role_name=role_name)
        db.session.add(role)
        db.session.commit()

    # Create a new user
    new_user = User(
        First_name=kwargs.get('First_name', ''),
        last_name=kwargs.get('last_name', ''),
        password=generate_password_hash(password),
        email=email,
        role=role,
        contact_number=kwargs.get('contact_number', ''),
        farm_location=kwargs.get('farm_location', ''),
        registration_date=datetime.utcnow(),
        status='Active',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        new_field=kwargs.get('new_field', '')
    )

    # Enable 2FA if specified
    if enable_2fa:
        totp = pyotp.TOTP(pyotp.random_base32())
        new_user.secret_2fa = totp.secret

        # Send 2FA code to the user's email
        subject = 'Two-Factor Authentication Code'
        body = f'Your 2FA code is: {totp.now()}'
        send_email(subject, email, body)

    # Add the user to the database
    db.session.add(new_user)
    db.session.commit()

    return new_user
def add_soil_parameters(user_id, nitrogen_level, phosphorus_level, potassium_level, temperature, humidity, ph_level, rainfall):
    # Check if the user exists
    user = User.query.get(user_id)
    if not user:
        raise ValueError('User not found.')

    # Create a new SoilParameters instance
    new_parameters = SoilParameters(
        user=user,
        nitrogen_level=nitrogen_level,
        phosphorus_level=phosphorus_level,
        potassium_level=potassium_level,
        temperature=temperature,
        humidity=humidity,
        ph_level=ph_level,
        rainfall=rainfall
    )

    # Add to the database
    db.session.add(new_parameters)
    db.session.commit()

    return new_parameters

def add_crop_details(crop_image, prediction_id):
    # Check if the prediction exists
    prediction = CropPrediction.query.get(prediction_id)
    if not prediction:
        raise ValueError('Prediction not found.')

    # Create a new CropDetails instance
    new_crop_details = CropDetails(
        crop_image=crop_image,
        prediction=prediction
    )

    # Add to the database
    db.session.add(new_crop_details)
    db.session.commit()

    return new_crop_details

def logout_user():
    # Clear the user session
    Session.clear()
    
