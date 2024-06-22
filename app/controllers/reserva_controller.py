from flask import jsonify, request

from app.services.reserva_service import ReservaService

reserva_service = ReservaService()


def get_all():
    reservas = reserva_service.fetch_all()
    return jsonify(reservas)


def get_by_id(reserva_id):
    reserva = reserva_service.fetch_by_id(reserva_id)
    if isinstance(reserva, dict):
        return jsonify(reserva)
    return reserva


def get_by_cliente_id(cliente_id):
    reservas = reserva_service.fetch_by_cliente_id(cliente_id)
    return jsonify(reservas)


def get_by_veiculo_id(veiculo_id):
    reservas = reserva_service.fetch_by_veiculo_id(veiculo_id)
    return jsonify(reservas)


def create():
    data = request.get_json()
    reserva = reserva_service.create(data)
    if isinstance(reserva, dict):
        return jsonify(reserva), 201  # Status code 201 for created
    return reserva


def update(reserva_id):
    data = request.get_json()
    reserva = reserva_service.update(reserva_id, data)
    if isinstance(reserva, dict):
        return jsonify(reserva)
    return reserva


def delete(reserva_id):
    result = reserva_service.delete(reserva_id)
    if result:
        return '', 204  # No content response for successful deletion
    return jsonify({'error': 'Reserva não encontrada'}), 404