from app.models import User
from app import db

def get_all_users():
    return User.query.all()
