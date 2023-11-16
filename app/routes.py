import datetime
from flask import jsonify, request
from app import app
# from app.db_operations import get_all_users
from app.models import Session, User
from app import db 
from werkzeug.security import generate_password_hash
# from app.services import add_crop_details, add_soil_parameters, login_user, logout_user, register_user


@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()

    # Check if the required fields are present
    if not all(field in data for field in ['email', 'password']):
        return jsonify({'error': 'Missing fields'}), 400

    email = data['email']
    password = data['password']

    # Find the user by their email
    user = User.query.filter_by(email=email).first()

    # If the user doesn't exist or the password is incorrect, return an error
    if not user or not user.check_password(password):
        return jsonify({'error': 'Invalid credentials'}), 401

    # Create a session for the user
    Session['user_id'] = user.id

    # Save the session in the database
    new_session = Session(
        user_id=user.id,
        login_timestamp=datetime.utcnow()
    )
    db.session.add(new_session)
    db.session.commit()

    return jsonify({'message': 'Logged in successfully'}), 200


@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()

    # Perform validation
    required_fields = ['First_name', 'last_name', 'password', 'email', 'contact_number', 'farmer_location']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing fields'}), 400

    # Additional validation (e.g., email format)
    if not is_valid_email(data['email']):
        return jsonify({'error': 'Invalid email format'}), 400

    try:
        # Check if the email already exists in the database
        existing_user = User.query.filter_by(email=data['email']).first()
        if existing_user:
            return jsonify({'error': 'Email already exists'}), 409  # 409: Conflict

        # Create a new user object and save it to the database
        new_user = User(
            First_name=data['First_name'],
            last_name=data['last_name'],
            password=generate_password_hash(data['password']),  # Hashing the password
            email=data['email'],
            role_id=1,  # Default role ID for a farmer
            contact_number=data['contact_number'],
            farmer_location=data['farmer_location']
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201  # 201: Created

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500  # 500: Internal Server Error

def is_valid_email(email):
    # Simple email format check (you can enhance this validation)
    return '@' in email



if __name__ == '__main__':
    app.run(debug= True)
