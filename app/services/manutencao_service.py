from app.repositorys.manutencao_repository import ManutencaoRepository
from flask import jsonify

class ManutencaoService:
    def __init__(self):
        self.repository = ManutencaoRepository()

    def to_dict(self, manutencao):
        return {
            'id': manutencao.id,
            'veiculo_id': manutencao.veiculo_id,
            'data_servico': manutencao.data_servico.isoformat(),
            'quilometragem': manutencao.quilometragem,
            'descricao': manutencao.descricao,
        }

    def error_response(self, message, status_code):
        response = jsonify({'error': message})
        response.status_code = status_code
        return response

    def fetch_all(self):
        manutencoes = self.repository.get_all()
        return [self.to_dict(manutecao) for manutecao in manutencoes]

    def create(self, data):
        veiculo_id = data.get('veiculo_id')
        data_servico = data.get('data_servico')
        quilometragem = data.get('quilometragem')
        descricao = data.get('descricao')

        if not veiculo_id or not data_servico or not quilometragem or not descricao:
            return self.error_response("Todos os campos são obrigatórios", 400)

        instance = self.repository.create(
            veiculo_id=veiculo_id,
            data_servico=data_servico,
            quilometragem=quilometragem,
            descricao=descricao
        )
        return self.to_dict(instance)

    def update(self, manutencao_id, data):
        manutencao = self.repository.get_by_id(manutencao_id)
        if manutencao is None:
            return self.error_response("Manutenção não encontrada", 404)
        
        veiculo_id = data.get('veiculo_id')
        data_servico = data.get('data_servico')
        quilometragem = data.get('quilometragem')
        descricao = data.get('descricao')

        if not veiculo_id or not data_servico or not quilometragem or not descricao:
            return self.error_response("Todos os campos são obrigatórios", 400)

        manutencao = self.repository.update(
            manutencao,
            veiculo_id=veiculo_id,
            data_servico=data_servico,
            quilometragem=quilometragem,
            descricao=descricao
        )
        return self.to_dict(manutencao)

    def fetch_by_id(self, manutencao_id):
        manutencao = self.repository.get_by_id(manutencao_id)
        if manutencao is None:
            return self.error_response("Manutenção não encontrada", 404)
        return self.to_dict(manutencao)

    def delete(self, manutencao_id):
        manutencao = self.repository.get_by_id(manutencao_id)
        if manutencao is None:
            return self.error_response("Manutenção não encontrada", 404)
        self.repository.delete(manutencao)
        return jsonify({'message': 'Manutenção excluída com sucesso'}), 200

    def fetch_by_veiculo_id(self, veiculo_id):
        manutencoes = self.repository.get_by_veiculo_id(veiculo_id)
        return [self.to_dict(manutencao) for manutencao in manutencoes]