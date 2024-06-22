from flask import Blueprint
from app.controllers.manutencao_controller import (
    create,
    update,
    delete,
    get_by_id,
    get_all,
    get_by_veiculo_id
)

manutencao_bp = Blueprint('manutencao_bp', __name__, url_prefix='/manutencoes')

manutencao_bp.route('/', methods=['POST'])(create)
manutencao_bp.route('/<int:manutencao_id>', methods=['PUT'])(update)
manutencao_bp.route('/<int:manutencao_id>', methods=['DELETE'])(delete)
manutencao_bp.route('/<int:manutencao_id>', methods=['GET'])(get_by_id)
manutencao_bp.route('/', methods=['GET'])(get_all)
manutencao_bp.route('/veiculo/<int:veiculo_id>', methods=['GET'])(get_by_veiculo_id)
