from flask import Blueprint, jsonify, request
from app.controllers.contrato_controller import (
    get_all_contratos,
    get_contrato_by_id,
    create_contrato,
    update_contrato,
    delete_contrato,
    get_contratos_by_reserva_id
)

contrato_bp = Blueprint('contrato_bp', __name__, url_prefix='/contratos')

contrato_bp.route('/', methods=['GET'])(get_all_contratos)
contrato_bp.route('/<int:contrato_id>', methods=['GET'])(get_contrato_by_id)
contrato_bp.route('/', methods=['POST'])(create_contrato)
contrato_bp.route('/<int:contrato_id>', methods=['PUT'])(update_contrato)
contrato_bp.route('/<int:contrato_id>', methods=['DELETE'])(delete_contrato)
contrato_bp.route('/reserva/<int:reserva_id>', methods=['GET'])(get_contratos_by_reserva_id)


