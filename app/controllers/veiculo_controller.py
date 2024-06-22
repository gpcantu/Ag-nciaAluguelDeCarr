from flask import jsonify, request
from app.services.veiculo_service import VeiculoService

veiculo_service = VeiculoService()

def get_all_veiculos():
    items = veiculo_service.fetch_all()
    return jsonify(items)

def get_veiculo_by_id(veiculo_id):
    item = veiculo_service.fetch_by_id(veiculo_id)
    if isinstance(item, dict):
        return jsonify(item)
    return item

def create_veiculo():
    data = request.get_json()
    item = veiculo_service.create(data)
    if isinstance(item, dict):
        return jsonify(item), 201
    return item

def update_veiculo(veiculo_id):
    data = request.get_json()
    item = veiculo_service.update(veiculo_id, data)
    if isinstance(item, dict):
        return jsonify(item)
    return '', 404

def delete_veiculo(veiculo_id):
    item = veiculo_service.delete(veiculo_id)
    if isinstance(item, tuple) and item[1] == 200:
        return '', 204
    return '', 404

def get_veiculo_by_marca_and_modelo():
    marca = request.args.get('marca')
    modelo = request.args.get('modelo')
    
    items = veiculo_service.fetch_by_marca_and_modelo(marca, modelo)
    return jsonify(items)