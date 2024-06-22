from flask import Blueprint
from app.controllers.cliente_controller import (
    get_all,
    get_by_id,
    create,
    update,
    delete,
    get_by_cpf,
    get_by_nome,
    get_by_email,
)

cliente_bp = Blueprint('cliente_bp', __name__, url_prefix='/clientes')

cliente_bp.route('/', methods=['GET'])(get_all)
cliente_bp.route('/<int:cliente_id>', methods=['GET'])(get_by_id)
cliente_bp.route('/', methods=['POST'])(create)
cliente_bp.route('/<int:cliente_id>', methods=['PUT'])(update)
cliente_bp.route('/<int:cliente_id>', methods=['DELETE'])(delete)

cliente_bp.route('/cpf/<string:cpf>', methods=['GET'])(get_by_cpf)
cliente_bp.route('/nome', methods=['GET'])(get_by_nome)
cliente_bp.route('/email/<string:email>', methods=['GET'])(get_by_email)

