from app.repositorys.base_repository import BaseRepository
from app.models.manutencao_model import Manutencao

class ManutencaoRepository(BaseRepository):
    def __init__(self):
        super().__init__(Manutencao)

    def get_by_veiculo_id(self, veiculo_id):
        return Manutencao.query.filter_by(veiculo_id=veiculo_id).all()