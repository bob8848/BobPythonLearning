# func_calculate_age.py
from datetime import datetime

def func_calculate_age(birthdate):
    today = datetime.today()
    birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

print(func_calculate_age('1990-01-01'))
