from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Импортирование всех функций из файлов для дб
from database.leaderservice import *
from database.questionservice import *
from database.registerservice import *