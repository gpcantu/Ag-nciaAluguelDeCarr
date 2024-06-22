from app.repositorys.reserva_repository import ReservaRepository
from flask import jsonify

class ReservaService:
    def __init__(self):
        self.repository = ReservaRepository()

    def to_dict(self, reserva):
        return {
            'id': reserva.id,
            'cliente_id': reserva.cliente_id,
            'veiculo_id': reserva.veiculo_id,
            'data_inicio': reserva.data_inicio.isoformat(),
            'data_fim': reserva.data_fim.isoformat(),
            'valor_total': reserva.valor_total,
            'status': reserva.status,
        }

    def error_response(self, message, status_code):
        response = jsonify({'error': message})
        response.status_code = status_code
        return response

    def fetch_all(self):
        reservas = self.repository.get_all()
        return [self.to_dict(reserva) for reserva in reservas]

    def fetch_by_id(self, reserva_id):
        reserva = self.repository.get_by_id(reserva_id)
        if not reserva:
            return self.error_response("Reserva não encontrada", 404)
        return self.to_dict(reserva)

    def fetch_by_cliente_id(self, cliente_id):
        reservas = self.repository.get_by_cliente_id(cliente_id)
        return [self.to_dict(reserva) for reserva in reservas]

    def fetch_by_veiculo_id(self, veiculo_id):
        reservas = self.repository.get_by_veiculo_id(veiculo_id)
        return [self.to_dict(reserva) for reserva in reservas]

    def create(self, data):
        cliente_id = data.get('cliente_id')
        veiculo_id = data.get('veiculo_id')
        data_inicio = data.get('data_inicio')
        data_fim = data.get('data_fim')
        valor_total = data.get('valor_total')
        status = data.get('status')

        if not cliente_id or not veiculo_id or not data_inicio or not data_fim or not valor_total or not status:
            return self.error_response("Todos os campos são obrigatórios", 400)

        instance = self.repository.create(
            cliente_id=cliente_id,
            veiculo_id=veiculo_id,
            data_inicio=data_inicio,
            data_fim=data_fim,
            valor_total=valor_total,
            status=status
        )
        return self.to_dict(instance)

    def update(self, reserva_id, data):
        reserva = self.repository.get_by_id(reserva_id)
        if not reserva:
            return self.error_response("Reserva não encontrada", 404)
        
        cliente_id = data.get('cliente_id')
        veiculo_id = data.get('veiculo_id')
        data_inicio = data.get('data_inicio')
        data_fim = data.get('data_fim')
        valor_total = data.get('valor_total')
        status = data.get('status')

        if not cliente_id or not veiculo_id or not data_inicio or not data_fim or not valor_total or not status:
            return self.error_response("Todos os campos são obrigatórios", 400)

        reserva = self.repository.update(
            reserva,
            cliente_id=cliente_id,
            veiculo_id=veiculo_id,
            data_inicio=data_inicio,
            data_fim=data_fim,
            valor_total=valor_total,
            status=status
        )
        return self.to_dict(reserva)

    def delete(self, reserva_id):
        reserva = self.repository.get_by_id(reserva_id)
        if not reserva:
            return self.error_response("Reserva não encontrada", 404)
        self.repository.delete(reserva)
        return jsonify({'message': 'Reserva excluída com sucesso'}), 200