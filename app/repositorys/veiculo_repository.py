from app.repositorys.base_repository import BaseRepository
from app.models.veiculo_model import Veiculo

class VeiculoRepository(BaseRepository):
    def __init__(self):
        super().__init__(Veiculo)

    def get_by_placa(self, placa):
        return Veiculo.query.filter_by(placa=placa).first()

    def get_by_marca_and_modelo(self, marca, modelo):
        return Veiculo.query.filter_by(marca=marca, modelo=modelo).all()
