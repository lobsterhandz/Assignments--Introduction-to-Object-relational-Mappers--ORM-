# routes_members.py: Handles CRUD operations for fitness center members, including validation and robust exception handling.

from flask import Blueprint, request, jsonify
from db import db
from models import Member
from validation import validate_email, validate_phone, validate_required_fields

# Create a Blueprint for organizing member-related routes.
members_bp = Blueprint('members', __name__)

# Route to add a new member.
@members_bp.route('/members', methods=['POST'])
def add_member():
    data = request.json

    # Validate required fields.
    valid, error_message = validate_required_fields(data, ['name', 'email', 'phone'])
    if not valid:
        return jsonify({'error': error_message}), 400

    # Validate email format.
    if not validate_email(data['email']):
        return jsonify({'error': 'Invalid email format.'}), 400

    # Validate phone format.
    if not validate_phone(data['phone']):
        return jsonify({'error': 'Invalid phone number format.'}), 400

    new_member = Member(name=data['name'], email=data['email'], phone=data['phone'])
    try:
        db.session.add(new_member)
        db.session.commit()
        return jsonify({'message': 'Member added successfully!'}), 201
    except Exception as e:
        return jsonify({'error': f'Failed to add member: {str(e)}'}), 500

# Route to get all members.
@members_bp.route('/members', methods=['GET'])
def get_members():
    try:
        members = Member.query.all()
        result = [{'id': member.id, 'name': member.name, 'email': member.email, 'phone': member.phone} for member in members]
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': f'Failed to retrieve members: {str(e)}'}), 500

# Route to get a member by ID.
@members_bp.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    try:
        member = Member.query.get_or_404(id)
        return jsonify({'id': member.id, 'name': member.name, 'email': member.email, 'phone': member.phone})
    except Exception as e:
        return jsonify({'error': f'Failed to retrieve member: {str(e)}'}), 500

# Route to update a member's information.
@members_bp.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    member = Member.query.get_or_404(id)
    data = request.json

    # Validate required fields.
    valid, error_message = validate_required_fields(data, ['name', 'email', 'phone'])
    if not valid:
        return jsonify({'error': error_message}), 400

    # Validate email format.
    if not validate_email(data['email']):
        return jsonify({'error': 'Invalid email format.'}), 400

    # Validate phone format.
    if not validate_phone(data['phone']):
        return jsonify({'error': 'Invalid phone number format.'}), 400

    member.name = data['name']
    member.email = data['email']
    member.phone = data['phone']
    try:
        db.session.commit()
        return jsonify({'message': 'Member updated successfully!'})
    except Exception as e:
        return jsonify({'error': f'Failed to update member: {str(e)}'}), 500

# Route to delete a member.
@members_bp.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    member = Member.query.get_or_404(id)
    try:
        db.session.delete(member)
        db.session.commit()
        return jsonify({'message': 'Member deleted successfully!'})
    except Exception as e:
        return jsonify({'error': f'Failed to delete member: {str(e)}'}), 500
