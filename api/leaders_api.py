from api import api_bp
from database import get_top_5_leaders_db
@api_bp.route('/leaders/<int:level>', methods=['GET'])
def get_top_5(level: int = 0):
    result = get_top_5_leaders_db(level)
    leaders = []
    # проходим по каждому объекту в списке result
    for leaders in result:
        print(leaders)
        leaders.append({leaders.user_fk.name: leaders.score})

    return {'level': level, 'leaders': None}
