from flask import jsonify, request
from app.services.seguro_service import SeguroService

seguro_service = SeguroService()

def get_seguro_by_tipo(tipo):
    seguro = seguro_service.fetch_by_tipo(tipo)
    if seguro:
        return jsonify(seguro_service.to_dict(seguro))
    else:
        return jsonify({'error': 'Seguro não encontrado'}), 404

def create_seguro():
    data = request.get_json()
    novo_seguro = seguro_service.create(data)
    return jsonify(novo_seguro), 201

def update_seguro(seguro_id):
    data = request.get_json()
    updated_seguro = seguro_service.update(seguro_id, data)
    return jsonify(updated_seguro)

def delete_seguro(seguro_id):
    delete_result = seguro_service.delete(seguro_id)
    if delete_result:
        return jsonify({'message': 'Seguro excluído com sucesso'})
    else:
        return jsonify({'error': 'Seguro não encontrado'}), 404