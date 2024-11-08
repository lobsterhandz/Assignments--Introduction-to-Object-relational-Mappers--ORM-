# models.py: Defines the database models used for Members and WorkoutSessions.

from db import db

# Member model to represent each fitness center member.
class Member(db.Model):
    # Define the table columns for the Member model.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Ensure name is provided.
    email = db.Column(db.String(100), unique=True, nullable=False)  # Email must be unique to avoid conflicts.
    phone = db.Column(db.String(20), nullable=False)

    # Edge Case Notes:
    # - Ensure name and email are not empty.
    # - Check email format before adding to database.
    # - Phone numbers should be validated for length and character content.

# WorkoutSession model to represent workout sessions for a specific member.
class WorkoutSession(db.Model):
    # Define the table columns for WorkoutSession model.
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    activity_type = db.Column(db.String(50), nullable=False)

    # Relationship to access the related member directly.
    member = db.relationship('Member', backref=db.backref('workout_sessions', lazy=True))

    # Edge Case Notes:
    # - Ensure member_id refers to an existing member (Foreign Key integrity).
    # - Date cannot be in the past (unless this is for a historical record).
    # - Duration should be a positive value greater than zero.
