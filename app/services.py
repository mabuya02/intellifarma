from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.models import SoilParameters

app = Flask(__name__)
db = SQLAlchemy(app)


def get_soil_parameters_for_user(user_id):
       
        soil_params = SoilParameters.query.filter_by(user_id=user_id).first()

        return soil_params  
