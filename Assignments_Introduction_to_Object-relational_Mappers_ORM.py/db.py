# db.py: This file sets up the database with SQLAlchemy and Marshmallow.
# Import necessary libraries for database setup.
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Instantiate the database (db) and serialization (ma) objects.
db = SQLAlchemy()
ma = Marshmallow()
