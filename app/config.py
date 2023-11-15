import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

DB_USERNAME = os.getenv('DB_USERNAME', 'default_username')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'default_password')
DB_NAME = os.getenv('DB_NAME', 'default_database_name')

# MySQL URI
SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@localhost:3306/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
