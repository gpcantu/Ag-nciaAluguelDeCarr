from flask import jsonify, request
from app.services.manutencao_service import ManutencaoService

manutencao_service = ManutencaoService()

def get_all():
    items = manutencao_service.fetch_all()
    return jsonify(items)

def get_by_id(manutencao_id):
    item = manutencao_service.fetch_by_id(manutencao_id)
    if isinstance(item, dict):
        return jsonify(item)
    return item

def create():
    data = request.get_json()
    item = manutencao_service.create(data)
    if isinstance(item, dict):
        return jsonify(item)
    return item

def update(manutencao_id):
    data = request.get_json()
    item = manutencao_service.update(manutencao_id, data)
    if isinstance(item, dict):
        return jsonify(item)
    return item

def delete(manutencao_id):
    item = manutencao_service.delete(manutencao_id)
    if item is None:
        return '', 204
    return item

def get_by_veiculo_id(veiculo_id):
    items = manutencao_service.fetch_by_veiculo_id(veiculo_id)
    return jsonify(items)
