from flask import Blueprint
from app.controllers.seguro_controller import (
    get_seguro_by_tipo,
    create_seguro,
    update_seguro,
    delete_seguro
)

seguro_bp = Blueprint('seguro_bp', __name__, url_prefix='/seguros')

seguro_bp.route('/tipo/<string:tipo>', methods=['GET'])(get_seguro_by_tipo)
seguro_bp.route('/', methods=['POST'])(create_seguro)
seguro_bp.route('/<int:seguro_id>', methods=['PUT'])(update_seguro)
seguro_bp.route('/<int:seguro_id>', methods=['DELETE'])(delete_seguro)
