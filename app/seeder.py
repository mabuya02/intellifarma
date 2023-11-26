from app.models import Role
from app import db

def seed_roles():
    roles = [
        Role(role_name='Admin'),
        Role(role_name='Farmer'),
    ]

    for role in roles:
        db.session.add(role)

    db.session.commit()
