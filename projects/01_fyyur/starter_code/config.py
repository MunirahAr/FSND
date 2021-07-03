import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
# TODO IMPLEMENT DATABASE URL

# I add postgresql url below as you show 
SQLALCHEMY_DATABASE_URI = '<postgresql://localhost/munsanadb?user=other&password=sss>'

# otherwise

SQLALCHEMY_DATABASE_URI = os.environ['mysql://munsana:123456@server/db']

if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://postgresql://localhost/munsanadb?user=other&password=sss", 1)

SQL_TRACK_MODIFICATIONS = False

