from flask import jsonify, request

from app.services.cliente_service import ClienteService

cliente_service = ClienteService()


def get_all():
    clientes = cliente_service.fetch_all()
    return jsonify(clientes)


def get_by_id(cliente_id):
    cliente = cliente_service.fetch_by_id(cliente_id)
    if cliente:
        return jsonify(cliente)
    return jsonify({'error': 'Cliente não encontrado'}), 404


def create():
    data = request.get_json()
    cliente = cliente_service.create(data)
    if isinstance(cliente, dict):
        return jsonify(cliente), 201  # Status code 201 for created
    return cliente


def update(cliente_id):
    data = request.get_json()
    cliente = cliente_service.update(cliente_id, data)
    if isinstance(cliente, dict):
        return jsonify(cliente)
    return cliente


def delete(cliente_id):
    result = cliente_service.delete(cliente_id)
    if result:
        return '', 204  # No content response for successful deletion
    return jsonify({'error': 'Cliente não encontrado'}), 404


def get_by_cpf(cpf):
    cliente = cliente_service.fetch_by_cpf(cpf)
    if cliente:
        return jsonify(cliente)
    return jsonify({'error': 'Cliente não encontrado'}), 404


def get_by_nome():
    nome = request.args.get('nome')
    if not nome:
        return jsonify({'error': 'Parâmetro "nome" é obrigatório'}), 400

    clientes = cliente_service.fetch_by_nome(nome)
    return jsonify(clientes)


def get_by_email(email):
    cliente = cliente_service.fetch_by_email(email)
    if cliente:
        return jsonify(cliente)
    return jsonify({'error': 'Cliente não encontrado'}), 404