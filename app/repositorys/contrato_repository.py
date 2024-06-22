from app.repositorys.base_repository import BaseRepository
from app.models.contrato_model import Contrato

class ContratoRepository(BaseRepository):
    def __init__(self):
        super().__init__(Contrato)

    def get_by_reserva_id(self, reserva_id):
        return Contrato.query.filter_by(reserva_id=reserva_id).all()
