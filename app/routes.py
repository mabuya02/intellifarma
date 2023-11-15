from flask import jsonify, request
from app import app
from app.db_operations import get_all_users
from app.services import add_crop_details, add_soil_parameters, login_user, logout_user, register_user



@app.route('/')
def hello_world():
    print("Root route accessed!")
    return 'Hello World'

@app.route('/api/login', methods=['POST'])
def api_login_user():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        # Call the login function
        authenticated_user, session = login_user(username, password)

        return jsonify({'message': 'Login successful', 'user_id': authenticated_user.id, 'session_id': session.id}), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 401

@app.route('/api/register', methods=['POST'])
def api_register_user():
    try:
        data = request.get_json()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        password = data.get('password')
        email = data.get('email')
        contact_number = data.get('contact_number')
        farm_location = data.get('farm_location')
        enable_2fa = data.get('enable_2fa', False)  

        # Call the register function
        new_user = register_user(
            first_name,
            last_name,
            password,
            email,
            contact_number=contact_number,
            farm_location=farm_location,
            enable_2fa=enable_2fa
        )

        return jsonify({'message': 'Registration successful', 'user_id': new_user.id}), 201

    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
@app.route('/api/add_soil_parameters', methods=['POST'])
def api_add_soil_parameters():
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        nitrogen_level = data.get('nitrogen_level')
        phosphorus_level = data.get('phosphorus_level')
        potassium_level = data.get('potassium_level')
        temperature = data.get('temperature')
        humidity = data.get('humidity')
        ph_level = data.get('ph_level')
        rainfall = data.get('rainfall')

        # Call the function to add soil parameters
        new_parameters = add_soil_parameters(
            user_id,
            nitrogen_level,
            phosphorus_level,
            potassium_level,
            temperature,
            humidity,
            ph_level,
            rainfall
        )

        return jsonify({'message': 'Soil parameters added successfully', 'parameters_id': new_parameters.id}), 201

    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/add_crop_details', methods=['POST'])
def api_add_crop_details():
    try:
        data = request.get_json()
        crop_image = data.get('crop_image')
        prediction_id = data.get('prediction_id')

        # Call the function to add crop details
        new_crop_details = add_crop_details(
            crop_image,
            prediction_id
        )

        return jsonify({'message': 'Crop details added successfully', 'crop_details_id': new_crop_details.id}), 201

    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/users', methods=['GET'])
def get_users():
    users = get_all_users()
    user_list = []
    for user in users:
        user_list.append({'id': user.id, 'First_name': user.First_name, 'email': user.email})
    return jsonify({'users': user_list})

# API endpoint for user logout
@app.route('/api/logout', methods=['POST'])
def api_logout_user():
    try:
        # Call the logout function
        logout_user()

        return jsonify({'message': 'Logout successful'}), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 401

if __name__ == '__main__':
    app.run(debug= True)
