from flask import Blueprint
from app.controllers.pagamento_controller import (
    get_pagamento_by_reserva_id,
    create_pagamento,
    update_pagamento,
    delete_pagamento
)

pagamento_bp = Blueprint('pagamento_bp', __name__, url_prefix='/pagamentos')

pagamento_bp.route('/reserva/<int:reserva_id>', methods=['GET'])(get_pagamento_by_reserva_id)
pagamento_bp.route('/', methods=['POST'])(create_pagamento)
pagamento_bp.route('/<int:pagamento_id>', methods=['PUT'])(update_pagamento)
pagamento_bp.route('/<int:pagamento_id>', methods=['DELETE'])(delete_pagamento)