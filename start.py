""" запуск застосунку 
при першому застосуванні відкрити рядки:
    "python manage.py migrate",
    "python manage.py createsuperuser",
поки що є сумніви щодо рядка 
    "docker-compose up -d",
"""

import os

commands = [
    "poetry update package",
    # "poetry shell",

# поки що є сумніви щодо рядка 
    "docker-compose up -d",

# при першому застосуванні відкрити рядки:
    "python manage.py migrate",
    "python manage.py createsuperuser",

    "python manage.py runserver",
]

def run_command(cmd):
    """запуск команди os.system"""
    print(f"Running command: {cmd}")
    os.system(cmd)


for command in commands:
    run_command(command)
