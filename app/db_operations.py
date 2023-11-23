from app.models import User
from app import db
from app.models import SoilParameters, User


def get_all_users():
    return User.query.all()

def get_soil_parameters_by_user(user_id):
    user_parameters = (
        SoilParameters.query
        .join(User)
        .filter(SoilParameters.user_id == user_id)
        .all()
    )
    return user_parameters

