from app import models
from app.db_operations import get_soil_parameters_by_user
from app import db  # Assuming this is where your SQLAlchemy instance resides


user_id = 123  # Replace with the actual user ID
user_soil_params = get_soil_parameters_by_user(user_id)
# Function to make predictions for a specific user_id
def predict_for_user(user_id):
    feature_list = []
    for param in user_soil_params:
        features = [
            param.nitrogen_level,
            param.phosphorus_level,
            param.potassium_level,
            param.temperature,
            param.humidity,
            param.ph_level,
            param.rainfall
        ]
        feature_list.append(features)

    # Prepare the data for prediction (convert to NumPy array or DataFrame)
    # Assuming 'model' is your trained machine learning model
    # Note: The exact data format needed might depend on how your model was trained
    # Convert feature_list to a NumPy array or DataFrame, similar to the one used for training
    
    # Make predictions
    predictions = models.predict(feature_list)

    return predictions
