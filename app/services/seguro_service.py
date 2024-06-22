from app.repositorys.seguro_repository import SeguroRepository
from flask import jsonify

class SeguroService:
    def __init__(self):
        self.repository = SeguroRepository()

    def to_dict(self, seguro):
        return {
            'id': seguro.id,
            'tipo': seguro.tipo,
            'valor': seguro.valor,
            'descricao': seguro.descricao,
        }

    def error_response(self, message, status_code):
        response = jsonify({'error': message})
        response.status_code = status_code
        return response

    def create(self, data):
        tipo = data.get('tipo')
        valor = data.get('valor')
        descricao = data.get('descricao')

        if not tipo or not valor or not descricao:
            return self.error_response("Todos os campos são obrigatórios", 400)

        instance = self.repository.create(
            tipo=tipo,
            valor=valor,
            descricao=descricao
        )
        return self.to_dict(instance)

    def update(self, seguro_id, data):
        seguro = self.repository.get_by_id(seguro_id)
        if seguro is None:
            return self.error_response("Seguro não encontrado", 404)
        
        tipo = data.get('tipo')
        valor = data.get('valor')
        descricao = data.get('descricao')

        if not tipo or not valor or not descricao:
            return self.error_response("Todos os campos são obrigatórios", 400)

        seguro = self.repository.update(
            seguro,
            tipo=tipo,
            valor=valor,
            descricao=descricao
        )
        return self.to_dict(seguro)

    def fetch_by_tipo(self, tipo):
        seguro = self.repository.get_by_tipo(tipo)
        return seguro

    def delete(self, seguro_id):
        seguro = self.repository.get_by_id(seguro_id)
        if seguro is None:
            return False
        self.repository.delete(seguro)
        return True