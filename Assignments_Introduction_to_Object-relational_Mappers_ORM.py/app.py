# app.py: The main application file that initializes and runs the Flask server.

from flask import Flask
from db import db, ma
from routes_members import members_bp
from routes_workouts import workouts_bp

# Initialize the Flask application.
app = Flask(__name__)

# Database configuration settings.
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:your_password@localhost/fitness_center_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Marshmallow with the Flask app.
db.init_app(app)
ma.init_app(app)

# Register the Blueprints for member and workout-related routes.
app.register_blueprint(members_bp)
app.register_blueprint(workouts_bp)

# Run the Flask application.
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create all database tables if they do not exist.
    app.run(debug=True)
