from database.models import Question
from database import db

# Функция добавления вопросов - 7 параметров
def add_question(main_text, variant_1, variant_2, variant_3, variant_4, correct_answer, level):
    new_question = Question(main_text=main_text, variant_1=variant_1, variant_2=variant_2, variant_3=variant_3, variant_4=variant_4,
                            correct_answer=correct_answer, level=level)
    db.session.add(new_question)
    db.session.commit()
# Вывести 20 вопросов - 1 параметр
def get_question(level):
    p = Question.query.filter_by(level=level).all()
    return p[0:21]
# Проверка ответов пользователя
def check_question(question_id, user_answer):
    f = Question.query.filter_by(id=question_id).first()
    if f.correct_answer == user_answer:
        return True
    else:
        return False