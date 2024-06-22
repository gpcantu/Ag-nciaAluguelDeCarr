from flask import jsonify, request
from app.services.contrato_service import ContratoService

contrato_service = ContratoService()

def get_all_contratos():
    contratos = contrato_service.fetch_all()
    return jsonify(contratos)

def get_contrato_by_id(contrato_id):
    contrato = contrato_service.fetch_by_id(contrato_id)
    if contrato:
        return jsonify(contrato)
    else:
        return jsonify({'error': 'Contrato não encontrado'}), 404

def create_contrato():
    data = request.get_json()
    novo_contrato = contrato_service.create(data)
    if isinstance(novo_contrato, dict):
        return jsonify(novo_contrato), 201
    return novo_contrato

def update_contrato(contrato_id):
    data = request.get_json()
    updated_contrato = contrato_service.update(contrato_id, data)
    if isinstance(updated_contrato, dict):
        return jsonify(updated_contrato)
    return updated_contrato

def delete_contrato(contrato_id):
    delete_result = contrato_service.delete(contrato_id)
    if delete_result:
        return jsonify({'message': 'Contrato excluído com sucesso'})
    else:
        return jsonify({'error': 'Contrato não encontrado'}), 404

def get_contratos_by_reserva_id(reserva_id):
    contratos = contrato_service.fetch_by_reserva_id(reserva_id)
    if isinstance(contratos, list):
        return jsonify(contratos)
    return contratos