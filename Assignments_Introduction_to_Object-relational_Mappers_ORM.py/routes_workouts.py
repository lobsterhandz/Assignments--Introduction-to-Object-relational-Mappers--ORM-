# routes_workouts.py: Handles CRUD operations for workout sessions, including validation and robust exception handling.

from flask import Blueprint, request, jsonify
from db import db
from models import WorkoutSession, Member
from validation import validate_date, validate_positive_integer, validate_required_fields

# Create a Blueprint for organizing workout-related routes.
workouts_bp = Blueprint('workouts', __name__)

# Route to add a new workout session.
@workouts_bp.route('/workouts', methods=['POST'])
def add_workout_session():
    data = request.json

    # Validate required fields.
    valid, error_message = validate_required_fields(data, ['member_id', 'date', 'duration_minutes', 'activity_type'])
    if not valid:
        return jsonify({'error': error_message}), 400

    # Validate date format.
    date = validate_date(data['date'])
    if not date:
        return jsonify({'error': 'Invalid date format. Should be YYYY-MM-DD HH:MM:SS'}), 400

    # Validate member ID existence.
    member = Member.query.get(data['member_id'])
    if not member:
        return jsonify({'error': 'Member not found for the given member ID.'}), 404

    # Validate duration.
    if not validate_positive_integer(data['duration_minutes']):
        return jsonify({'error': 'Duration must be a positive integer.'}), 400

    new_session = WorkoutSession(
        member_id=data['member_id'],
        date=date,
        duration_minutes=data['duration_minutes'],
        activity_type=data['activity_type']
    )
    try:
        db.session.add(new_session)
        db.session.commit()
        return jsonify({'message': 'Workout session added successfully!'}), 201
    except Exception as e:
        return jsonify({'error': f'Failed to add workout session: {str(e)}'}), 500

# Route to get all workout sessions.
@workouts_bp.route('/workouts', methods=['GET'])
def get_workout_sessions():
    try:
        sessions = WorkoutSession.query.all()
        result = [
            {
                'id': session.id,
                'member_id': session.member_id,
                'date': session.date.strftime("%Y-%m-%d %H:%M:%S"),
                'duration_minutes': session.duration_minutes,
                'activity_type': session.activity_type
            } for session in sessions
        ]
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': f'Failed to retrieve workout sessions: {str(e)}'}), 500

# Route to get all workout sessions for a specific member.
@workouts_bp.route('/members/<int:member_id>/workouts', methods=['GET'])
def get_workouts_for_member(member_id):
    try:
        member = Member.query.get_or_404(member_id)
        result = [
            {
                'id': session.id,
                'date': session.date.strftime("%Y-%m-%d %H:%M:%S"),
                'duration_minutes': session.duration_minutes,
                'activity_type': session.activity_type
            } for session in member.workout_sessions
        ]
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': f'Failed to retrieve workouts for member: {str(e)}'}), 500
