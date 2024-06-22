from flask import Blueprint
from app.controllers.rastreamento_controller import (
    get_rastreamento_by_veiculo_id,
    create_rastreamento,
    update_rastreamento,
    delete_rastreamento
)

rastreamento_bp = Blueprint('rastreamento_bp', __name__, url_prefix='/rastreamentos')

rastreamento_bp.route('/veiculo/<int:veiculo_id>', methods=['GET'])(get_rastreamento_by_veiculo_id)
rastreamento_bp.route('/', methods=['POST'])(create_rastreamento)
rastreamento_bp.route('/<int:rastreamento_id>', methods=['PUT'])(update_rastreamento)
rastreamento_bp.route('/<int:rastreamento_id>', methods=['DELETE'])(delete_rastreamento)
