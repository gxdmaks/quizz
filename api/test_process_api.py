from api import api_bp
from database import get_question, user_end_test_db, check_question

@api_bp.route('/get-questions/<int:level>', methods=['GET'])
def get_questions(level: int):
    result = get_question(level)

    return {'status': 1, 'questions': result}

@api_bp.route('/check-answer/<int:question_id>/<int:user_answer>', methods=['POST'])
def check_user_answer(question_id: int, user_answer: int):
    result = check_question(question_id, user_answer)
    if result:
        return {'status': 1}
    else:
        return {'status': 0}

@api_bp.route('/done/<int:user_id>/<int:correct_answer>/<int:level>', methods=['POST'])
def commit_user_answers(user_id: int, correct_answer: int, level: int):
    result = user_end_test_db(user_id, correct_answer, level)

    return {'status': 1, 'correct_answer': correct_answer, 'position_on_top': result} 
