from flask import Blueprint
from app.controllers.reserva_controller import (
    get_all,
    get_by_id,
    get_by_cliente_id,
    get_by_veiculo_id,
    create,
    update,
    delete
)

reserva_bp = Blueprint('reserva_bp', __name__, url_prefix='/reservas')

reserva_bp.route('/', methods=['GET'])(get_all)
reserva_bp.route('/<int:reserva_id>', methods=['GET'])(get_by_id)
reserva_bp.route('/cliente/<int:cliente_id>', methods=['GET'])(get_by_cliente_id)
reserva_bp.route('/veiculo/<int:veiculo_id>', methods=['GET'])(get_by_veiculo_id)
reserva_bp.route('/', methods=['POST'])(create)
reserva_bp.route('/<int:reserva_id>', methods=['PUT'])(update)
reserva_bp.route('/<int:reserva_id>', methods=['DELETE'])(delete)