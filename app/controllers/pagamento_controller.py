from flask import jsonify, request
from app.services.pagamento_service import PagamentoService

pagamento_service = PagamentoService()

def get_pagamento_by_reserva_id(reserva_id):
    pagamento = pagamento_service.fetch_by_reserva_id(reserva_id)
    if pagamento:
        return jsonify(pagamento_service.to_dict(pagamento))
    else:
        return jsonify({'error': 'Pagamento não encontrado'}), 404

def create_pagamento():
    data = request.get_json()
    novo_pagamento = pagamento_service.create(data)
    return jsonify(novo_pagamento), 201

def update_pagamento(pagamento_id):
    data = request.get_json()
    updated_pagamento = pagamento_service.update(pagamento_id, data)
    return jsonify(updated_pagamento)

def delete_pagamento(pagamento_id):
    delete_result = pagamento_service.delete(pagamento_id)
    if delete_result:
        return jsonify({'message': 'Pagamento excluído com sucesso'})
    else:
        return jsonify({'error': 'Pagamento não encontrado'}), 404