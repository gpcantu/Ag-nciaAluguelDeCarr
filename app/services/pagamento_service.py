from app.repositorys.pagamento_repository import PagamentoRepository
from flask import jsonify

class PagamentoService:
    def __init__(self):
        self.repository = PagamentoRepository()

    def to_dict(self, pagamento):
        return {
            'id': pagamento.id,
            'reserva_id': pagamento.reserva_id,
            'valor_pago': pagamento.valor_pago,
            'data_pagamento': pagamento.data_pagamento.isoformat(),
            'metodo_pagamento': pagamento.metodo_pagamento,
        }

    def error_response(self, message, status_code):
        response = jsonify({'error': message})
        response.status_code = status_code
        return response

    def create(self, data):
        reserva_id = data.get('reserva_id')
        valor_pago = data.get('valor_pago')
        data_pagamento = data.get('data_pagamento')
        metodo_pagamento = data.get('metodo_pagamento')

        if not reserva_id or not valor_pago or not data_pagamento or not metodo_pagamento:
            return self.error_response("Todos os campos são obrigatórios", 400)

        instance = self.repository.create(
            reserva_id=reserva_id,
            valor_pago=valor_pago,
            data_pagamento=data_pagamento,
            metodo_pagamento=metodo_pagamento
        )
        return self.to_dict(instance)

    def update(self, pagamento_id, data):
        pagamento = self.repository.get_by_id(pagamento_id)
        if pagamento is None:
            return self.error_response("Pagamento não encontrado", 404)
        
        reserva_id = data.get('reserva_id')
        valor_pago = data.get('valor_pago')
        data_pagamento = data.get('data_pagamento')
        metodo_pagamento = data.get('metodo_pagamento')

        if not reserva_id or not valor_pago or not data_pagamento or not metodo_pagamento:
            return self.error_response("Todos os campos são obrigatórios", 400)

        pagamento = self.repository.update(
            pagamento,
            reserva_id=reserva_id,
            valor_pago=valor_pago,
            data_pagamento=data_pagamento,
            metodo_pagamento=metodo_pagamento
        )
        return self.to_dict(pagamento)

    def fetch_by_id(self, pagamento_id):
        pagamento = self.repository.get_by_id(pagamento_id)
        if pagamento is None:
            return self.error_response("Pagamento não encontrado", 404)
        return self.to_dict(pagamento)

    def delete(self, pagamento_id):
        pagamento = self.repository.get_by_id(pagamento_id)
        if pagamento is None:
            return self.error_response("Pagamento não encontrado", 404)
        self.repository.delete(pagamento)
        return jsonify({'message': 'Pagamento excluído com sucesso'}), 200