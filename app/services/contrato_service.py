from app.repositorys.contrato_repository import ContratoRepository
from flask import jsonify

class ContratoService:
    def __init__(self):
        self.repository = ContratoRepository()

    def to_dict(self, contrato):
        return {
            'id': contrato.id,
            'reserva_id': contrato.reserva_id,
            'termos_condicoes': contrato.termos_condicoes,
        }

    def error_response(self, message, status_code):
        response = jsonify({'error': message})
        response.status_code = status_code
        return response

    def fetch_all(self):
        contratos = self.repository.get_all()
        return [self.to_dict(contrato) for contrato in contratos]

    def create(self, data):
        reserva_id = data.get('reserva_id')
        termos_condicoes = data.get('termos_condicoes')

        if not reserva_id or not termos_condicoes:
            return self.error_response("Todos os campos são obrigatórios", 400)

        instance = self.repository.create(
            reserva_id=reserva_id,
            termos_condicoes=termos_condicoes
        )
        return self.to_dict(instance)

    def update(self, contrato_id, data):
        contrato = self.repository.get_by_id(contrato_id)
        if contrato is None:
            return self.error_response("Contrato não encontrado", 404)
        
        reserva_id = data.get('reserva_id')
        termos_condicoes = data.get('termos_condicoes')

        if not reserva_id or not termos_condicoes:
            return self.error_response("Todos os campos são obrigatórios", 400)

        contrato = self.repository.update(
            contrato,
            reserva_id=reserva_id,
            termos_condicoes=termos_condicoes
        )
        return self.to_dict(contrato)

    def fetch_by_id(self, contrato_id):
        contrato = self.repository.get_by_id(contrato_id)
        if contrato is None:
            return self.error_response("Contrato não encontrado", 404)
        return self.to_dict(contrato)

    def delete(self, contrato_id):
        contrato = self.repository.get_by_id(contrato_id)
        if contrato is None:
            return self.error_response("Contrato não encontrado", 404)
        self.repository.delete(contrato)
        return jsonify({'message': 'Contrato excluído com sucesso'}), 200

    def fetch_by_reserva_id(self, reserva_id):
        contratos = self.repository.get_by_reserva_id(reserva_id)
        if not contratos:
            return self.error_response("Contratos não encontrados para a reserva especificada", 404)
        return [self.to_dict(contrato) for contrato in contratos]