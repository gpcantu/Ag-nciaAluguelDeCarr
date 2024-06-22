from app.repositorys.base_repository import BaseRepository
from app.models.rastreamento_model import Rastreamento

class RastreamentoRepository(BaseRepository):
    def __init__(self):
        super().__init__(Rastreamento)

    def get_by_veiculo_id(self, veiculo_id):
        return Rastreamento.query.filter_by(veiculo_id=veiculo_id).all()
