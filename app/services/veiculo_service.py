from app.repositorys.veiculo_repository import VeiculoRepository
from flask import jsonify

class VeiculoService:
    def __init__(self):
        self.repository = VeiculoRepository()

    def to_dict(self, veiculo):
        return {
            'id': veiculo.id,
            'marca': veiculo.marca,
            'modelo': veiculo.modelo,
            'ano': veiculo.ano,
            'placa': veiculo.placa,
            'quilometragem': veiculo.quilometragem,
        }

    def error_response(self, message, status_code):
        response = jsonify({'error': message})
        response.status_code = status_code
        return response

    def fetch_all(self):
        veiculos = self.repository.get_all()
        return [self.to_dict(veiculo) for veiculo in veiculos]

    def fetch_by_id(self, veiculo_id):
        veiculo = self.repository.get_by_id(veiculo_id)
        if veiculo is None:
            return self.error_response("Veículo não encontrado", 404)
        return self.to_dict(veiculo)

    def create(self, data):
        marca = data.get('marca')
        modelo = data.get('modelo')
        ano = data.get('ano')
        placa = data.get('placa')
        quilometragem = data.get('quilometragem')

        if not marca or not modelo or not ano or not placa or not quilometragem:
            return self.error_response("Todos os campos são obrigatórios", 400)

        instance = self.repository.create(
            marca=marca,
            modelo=modelo,
            ano=ano,
            placa=placa,
            quilometragem=quilometragem
        )
        return self.to_dict(instance)

    def update(self, veiculo_id, data):
        veiculo = self.repository.get_by_id(veiculo_id)
        if veiculo is None:
            return self.error_response("Veículo não encontrado", 404)
        
        marca = data.get('marca')
        modelo = data.get('modelo')
        ano = data.get('ano')
        placa = data.get('placa')
        quilometragem = data.get('quilometragem')

        if not marca or not modelo or not ano or not placa or not quilometragem:
            return self.error_response("Todos os campos são obrigatórios", 400)

        veiculo = self.repository.update(
            veiculo,
            marca=marca,
            modelo=modelo,
            ano=ano,
            placa=placa,
            quilometragem=quilometragem
        )
        return self.to_dict(veiculo)

    def delete(self, veiculo_id):
        veiculo = self.repository.get_by_id(veiculo_id)
        if veiculo is None:
            return self.error_response("Veículo não encontrado", 404)
        self.repository.delete(veiculo)
        return jsonify({'message': 'Veículo excluído com sucesso'}), 200

    def fetch_by_marca_and_modelo(self, marca, modelo):
        veiculos = self.repository.get_by_marca_and_modelo(marca, modelo)
        return [self.to_dict(veiculo) for veiculo in veiculos]