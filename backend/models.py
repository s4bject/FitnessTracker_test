# models.py
# Модели данных (используется pg8000)
class User:
    def __init__(self, user_id, username, email, age, weight, height):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.age = age
        self.weight = weight
        self.height = height

class Exercise:
    def __init__(self, exercise_id, user_id, exercise_type, duration, date):
        self.exercise_id = exercise_id
        self.user_id = user_id
        self.exercise_type = exercise_type
        self.duration = duration
        self.date = date

class Diet:
    def __init__(self, diet_id, user_id, meal, calories, date):
        self.diet_id = diet_id
        self.user_id = user_id
        self.meal = meal
        self.calories = calories
        self.date = date

class Progress:
    def __init__(self, progress_id, user_id, weight, date):
        self.progress_id = progress_id
        self.user_id = user_id
        self.weight = weight
        self.date = date