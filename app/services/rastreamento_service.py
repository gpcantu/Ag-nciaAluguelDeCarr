from app.repositorys.rastreamento_repository import RastreamentoRepository
from flask import jsonify

class RastreamentoService:
    def __init__(self):
        self.repository = RastreamentoRepository()

    def to_dict(self, rastreamento):
        return {
            'id': rastreamento.id,
            'veiculo_id': rastreamento.veiculo_id,
            'data_hora': rastreamento.data_hora.isoformat(),
            'latitude': rastreamento.latitude,
            'longitude': rastreamento.longitude,
        }

    def error_response(self, message, status_code):
        response = jsonify({'error': message})
        response.status_code = status_code
        return response

    def create(self, data):
        veiculo_id = data.get('veiculo_id')
        data_hora = data.get('data_hora')
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        if not veiculo_id or not data_hora or not latitude or not longitude:
            return self.error_response("Todos os campos são obrigatórios", 400)

        instance = self.repository.create(
            veiculo_id=veiculo_id,
            data_hora=data_hora,
            latitude=latitude,
            longitude=longitude
        )
        return self.to_dict(instance)

    def update(self, rastreamento_id, data):
        rastreamento = self.repository.get_by_id(rastreamento_id)
        if rastreamento is None:
            return self.error_response("Rastreamento não encontrado", 404)
        
        veiculo_id = data.get('veiculo_id')
        data_hora = data.get('data_hora')
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        if not veiculo_id or not data_hora or not latitude or not longitude:
            return self.error_response("Todos os campos são obrigatórios", 400)

        rastreamento = self.repository.update(
            rastreamento,
            veiculo_id=veiculo_id,
            data_hora=data_hora,
            latitude=latitude,
            longitude=longitude
        )
        return self.to_dict(rastreamento)

    def fetch_by_id(self, rastreamento_id):
        rastreamento = self.repository.get_by_id(rastreamento_id)
        if rastreamento is None:
            return self.error_response("Rastreamento não encontrado", 404)
        return self.to_dict(rastreamento)

    def fetch_by_veiculo_id(self, veiculo_id):
        rastreamentos = self.repository.get_by_veiculo_id(veiculo_id)
        if not rastreamentos:
            return None
        return [self.to_dict(r) for r in rastreamentos]

    def delete(self, rastreamento_id):
        rastreamento = self.repository.get_by_id(rastreamento_id)
        if rastreamento is None:
            return self.error_response("Rastreamento não encontrado", 404)
        self.repository.delete(rastreamento)
        return jsonify({'message': 'Rastreamento excluído com sucesso'}), 200