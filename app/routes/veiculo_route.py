from flask import Blueprint
from app.controllers.veiculo_controller import (
    get_all_veiculos,
    get_veiculo_by_id,
    create_veiculo,
    update_veiculo,
    delete_veiculo,
    get_veiculo_by_marca_and_modelo
)

veiculo_bp = Blueprint('veiculo_bp', __name__, url_prefix='/veiculos')

veiculo_bp.route('/', methods=['GET'])(get_all_veiculos)
veiculo_bp.route('/<int:veiculo_id>', methods=['GET'])(get_veiculo_by_id)
veiculo_bp.route('/', methods=['POST'])(create_veiculo)
veiculo_bp.route('/<int:veiculo_id>', methods=['PUT'])(update_veiculo)
veiculo_bp.route('/<int:veiculo_id>', methods=['DELETE'])(delete_veiculo)
veiculo_bp.route('/marca_modelo', methods=['GET'])(get_veiculo_by_marca_and_modelo)
