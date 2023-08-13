from database.models import User
from database import db
def register_user_db(name, phone_number):
    # проверка пользователя на наличие в базе
    checker = User.query.filter_by(phone_number=phone_number).first()
    # если есть пользователь
    if checker:
        return checker.id
    # Добавление данных
    new_user = User(name=name, phone_number=phone_number)
    db.session.add(new_user)
    db.session.commit()

    return new_user.id
