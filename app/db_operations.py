from app.models import Review, User
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


def get_all_user_reviews(user_id):
    user_reviews = {
        Review.query
        .join(User)
        .filter(Review.user_id == user_id)
        .all()
    }
    
    return user_reviews


  # Fetch only the first (latest) entry
def get_latest_soil_parameters_by_user(user_id):
    latest_param = (
        db.session.query(SoilParameters)
        .filter_by(user_id=user_id)
        .order_by(SoilParameters.created_at.desc())  
        .first()
    )
    return latest_param

