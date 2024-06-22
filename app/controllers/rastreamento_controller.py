from flask import jsonify, request
from app.services.rastreamento_service import RastreamentoService

rastreamento_service = RastreamentoService()

def get_rastreamento_by_veiculo_id(veiculo_id):
    rastreamentos = rastreamento_service.fetch_by_veiculo_id(veiculo_id)
    if rastreamentos:
        return jsonify(rastreamentos)
    else:
        return jsonify({'error': 'Rastreamentos não encontrados'}), 404

def create_rastreamento():
    data = request.get_json()
    novo_rastreamento = rastreamento_service.create(data)
    return jsonify(novo_rastreamento), 201

def update_rastreamento(rastreamento_id):
    data = request.get_json()
    updated_rastreamento = rastreamento_service.update(rastreamento_id, data)
    return jsonify(updated_rastreamento)

def delete_rastreamento(rastreamento_id):
    delete_result = rastreamento_service.delete(rastreamento_id)
    if delete_result:
        return jsonify({'message': 'Rastreamento excluído com sucesso'})
    else:
        return jsonify({'error': 'Rastreamento não encontrado'}), 404