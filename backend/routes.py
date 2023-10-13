from flask import Blueprint, jsonify, request
from pg8000 import connect, DatabaseError
from models import User,Exercise,Diet,Progress

app = Blueprint('routes_app', __name__)

# Настройте параметры подключения к PostgreSQL
postgres_config = {
    'host': 'localhost',
    'user': 's4bject',
    'password': 'sdds234432',
    'database': 'fitnesstracker'
}

# Создайте соединение с базой данных
try:
    conn = connect(**postgres_config)
    print("Successfully connected to PostgreSQL")
except DatabaseError:
    print("Failed to connect to PostgreSQL")

@app.route('/users', methods=['GET'])
def get_users():
    """Получить данные всех пользователей."""
    try:
        conn = connect(**postgres_config)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        data = cursor.fetchall()
        cursor.close()
        return jsonify({'data': data}), 200
    except DatabaseError as e:
        return jsonify(message=f"Database error: {str(e)}"), 500
    finally:
        conn.close()

@app.route('/users', methods=['POST'])
def create_user():
    """Создать нового пользователя."""
    user_data = request.json
    user = User(
        user_id=user_data['id'],
        username=user_data['username'],
        email=user_data['email'],
        age=user_data['age'],
        weight=user_data['weight'],
        height=user_data['height']
    )

    try:
        conn = connect(**postgres_config)
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO users (id, username, email, age, weight, height) VALUES (%s, %s, %s, %s, %s, %s)',
            (user.user_id, user.username, user.email, user.age, user.weight, user.height))
        conn.commit()
        cursor.close()
        return jsonify(message="User data saved successfully"), 200
    except DatabaseError as e:
        return jsonify(message=f"Database error: {str(e)}"), 500
    finally:
        conn.close()

@app.route('/exercises', methods=['GET'])
def get_exercises():
    """Получить данные о тренировках."""
    try:
        conn = connect(**postgres_config)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM exercises')
        data = cursor.fetchall()
        cursor.close()
        return jsonify({'data': data}), 200
    except DatabaseError as e:
        return jsonify(message=f"Database error: {str(e)}"), 500
    finally:
        conn.close()

@app.route('/exercises', methods=['POST'])
def create_exercise():
    """Создать новую тренировку."""
    exercise_data = request.json
    exercise = Exercise(
        exercise_id=exercise_data['exercise_id'],
        user_id=exercise_data['user_id'],
        exercise_type=exercise_data['exercise_type'],
        duration=exercise_data['duration'],
        date=exercise_data['date']
    )

    try:
        conn = connect(**postgres_config)
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO exercises (exercise_id, user_id, exercise_type, duration, date) VALUES (%s, %s, %s, %s, %s)',
            (exercise.exercise_id, exercise.user_id, exercise.exercise_type, exercise.duration, exercise.date))
        conn.commit()
        cursor.close()
        return jsonify(message="Exercise data saved successfully"), 200
    except DatabaseError as e:
        return jsonify(message=f"Database error: {str(e)}"), 500
    finally:
        conn.close()
@app.route('/diet', methods=['GET'])
def get_diet():
    """Получить данные о питании."""
    try:
        conn = connect(**postgres_config)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM diet')
        data = cursor.fetchall()
        cursor.close()
        return jsonify({'data': data}), 200
    except DatabaseError as e:
        return jsonify(message=f"Database error: {str(e)}"), 500
    finally:
        conn.close()

@app.route('/diet', methods=['POST'])
def create_diet():
    """Создать новую запись о питании."""
    diet_data = request.json
    diet = Diet(
        diet_id=diet_data['id'],
        user_id=diet_data['user_id'],
        meal=diet_data['meal'],
        calories=diet_data['calories'],
        date=diet_data['date']
    )

    try:
        conn = connect(**postgres_config)
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO diet (id, user_id, meal, calories, date) VALUES (%s, %s, %s, %s, %s)',
            (diet.diet_id, diet.user_id, diet.meal, diet.calories, diet.date))
        conn.commit()
        cursor.close()
        return jsonify(message="Diet data saved successfully"), 200
    except DatabaseError as e:
        return jsonify(message=f"Database error: {str(e)}"), 500
    finally:
        conn.close()
@app.route('/progress', methods=['GET'])
def get_progress():
    """Получить данные о прогрессе."""
    try:
        conn = connect(**postgres_config)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM progress')
        data = cursor.fetchall()
        cursor.close()
        return jsonify({'data': data}), 200
    except DatabaseError as e:
        return jsonify(message=f"Database error: {str(e)}"), 500
    finally:
        conn.close()

@app.route('/progress', methods=['POST'])
def create_progress():
    """Создать новую запись о прогрессе."""
    progress_data = request.json
    progress = Progress(
        progress_id=progress_data['id'],
        user_id=progress_data['user_id'],
        weight=progress_data['weight'],
        date=progress_data['date']
    )

    try:
        conn = connect(**postgres_config)
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO progress (id, user_id, weight, date) VALUES (%s, %s, %s, %s)',
            (progress.progress_id, progress.user_id, progress.weight, progress.date))
        conn.commit()
        cursor.close()
        return jsonify(message="Progress data saved successfully"), 200
    except DatabaseError as e:
        return jsonify(message=f"Database error: {str(e)}"), 500
    finally:
        conn.close()