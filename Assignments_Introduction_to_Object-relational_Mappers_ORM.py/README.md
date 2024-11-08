# Fitness Center Management API - Flask-SQLAlchemy

## Overview
This project is a Flask-based RESTful API for managing a fitness center's database. It uses Flask-SQLAlchemy for ORM (Object-Relational Mapping) to simplify database management and allows you to interact with `Members` and `WorkoutSessions` tables through API endpoints. The project is organized modularly for easier maintenance and scalability.

### Key Features
- Flask application with a modular structure to enhance maintainability.
- `Members` and `WorkoutSessions` database models using Flask-SQLAlchemy.
- CRUD operations for `Members` and `WorkoutSessions` through RESTful API endpoints.
- Input validation to ensure data integrity.
- Robust error and exception handling for increased resilience.

## Directory Structure
```
fitness_center_api/
|
├── app.py                 # Main application file
├── db.py                  # Database setup
├── models.py              # SQLAlchemy models
├── routes_members.py      # Routes for managing members
├── routes_workouts.py     # Routes for managing workout sessions
├── validation.py          # Validation utilities
└── venv/                  # Virtual environment (not included in Git)
```

## Installation & Setup

1. **Clone the Repository**
    ```sh
    git clone <repository-url>
    cd fitness_center_api
    ```

2. **Create a Virtual Environment**
    ```sh
    python -m venv venv
    ```

3. **Activate the Virtual Environment**
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

4. **Install Required Dependencies**
    ```sh
    pip install -r requirements.txt
    ```
    *Note:* If you do not have a `requirements.txt` file, you can install the dependencies manually:
    ```sh
    pip install Flask Flask-SQLAlchemy Flask-Marshmallow mysql-connector-python
    ```

5. **Database Setup**
   - Ensure you have a MySQL database server running.
   - Update `app.py` with your MySQL credentials:
     ```python
     app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:your_password@localhost/fitness_center_db'
     ```

6. **Run the Application**
   ```sh
   python app.py
   ```
   *The application will run by default on [http://127.0.0.1:5000](http://127.0.0.1:5000)*

## Endpoints Overview

### Member Endpoints

1. **Add Member**
    - `POST /members`
    - **Request Body**:
      ```json
      {
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "1234567890"
      }
      ```
    - **Response**:
      - 201: Member added successfully
      - 400: Missing required fields or invalid data

2. **Get All Members**
    - `GET /members`
    - **Response**:
      - 200: List of members
      - 500: Server error

3. **Get Member by ID**
    - `GET /members/<int:id>`
    - **Response**:
      - 200: Member details
      - 404: Member not found

4. **Update Member**
    - `PUT /members/<int:id>`
    - **Request Body**:
      ```json
      {
        "name": "John Updated",
        "email": "john.updated@example.com",
        "phone": "0987654321"
      }
      ```
    - **Response**:
      - 200: Member updated successfully
      - 400: Missing required fields or invalid data
      - 404: Member not found

5. **Delete Member**
    - `DELETE /members/<int:id>`
    - **Response**:
      - 200: Member deleted successfully
      - 404: Member not found

### Workout Session Endpoints

1. **Add Workout Session**
    - `POST /workouts`
    - **Request Body**:
      ```json
      {
        "member_id": 1,
        "date": "2024-11-05 14:00:00",
        "duration_minutes": 60,
        "activity_type": "Yoga"
      }
      ```
    - **Response**:
      - 201: Workout session added successfully
      - 400: Missing required fields or invalid data
      - 404: Member not found

2. **Get All Workout Sessions**
    - `GET /workouts`
    - **Response**:
      - 200: List of workout sessions
      - 500: Server error

3. **Get All Workout Sessions for a Member**
    - `GET /members/<int:member_id>/workouts`
    - **Response**:
      - 200: List of workout sessions for the member
      - 404: Member not found

## Validation & Error Handling
- **Validation** is done using functions in `validation.py` to ensure data integrity:
  - Email format is checked.
  - Phone numbers are validated for correct length and characters.
  - Dates must follow the `YYYY-MM-DD HH:MM:SS` format.
  - Required fields must be present.
- **Exception Handling** is implemented across the application to handle edge cases such as:
  - Missing fields or invalid data formats.
  - Foreign key violations (e.g., adding a workout session for a non-existent member).
  - Database errors or connection issues.

## Running Tests
You can manually test the API using tools like [Postman](https://www.postman.com/) or [cURL](https://curl.se/). Make sure the server is running locally before testing.

Example cURL request to add a member:
```sh
curl -X POST http://127.0.0.1:5000/members \
-H "Content-Type: application/json" \
-d '{"name": "Jane Doe", "email": "jane@example.com", "phone": "1234567890"}'
```

## Future Enhancements
- Implement user authentication (e.g., JWT) to secure the API.
- Add pagination to the `GET` endpoints to handle large datasets.
- Deploy the API using a platform like AWS, Azure, or Heroku for production use.

## Troubleshooting
- **Database Connection Issues**: Ensure the MySQL server is running, and credentials in `app.py` are correct.
- **Module Not Found**: Verify that you are in the virtual environment and all dependencies are installed.

## License
This project is licensed under the MIT License.

## Author
Jose and ChatGPT

If you have any issues, suggestions, or improvements, feel free to contribute or contact me!

