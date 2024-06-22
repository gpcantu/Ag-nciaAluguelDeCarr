from flask import Blueprint
from app.controllers.feedback_controller import (
    get_all,
    get_by_id,
    get_by_cliente_id,
    create,
    update,
    delete
)

feedback_bp = Blueprint('feedback_bp', __name__, url_prefix='/feedbacks')

feedback_bp.route('/', methods=['GET'])(get_all)
feedback_bp.route('/<int:feedback_id>', methods=['GET'])(get_by_id)
feedback_bp.route('/cliente/<int:cliente_id>', methods=['GET'])(get_by_cliente_id)
feedback_bp.route('/', methods=['POST'])(create)
feedback_bp.route('/<int:feedback_id>', methods=['PUT'])(update)
feedback_bp.route('/<int:feedback_id>', methods=['DELETE'])(delete)
