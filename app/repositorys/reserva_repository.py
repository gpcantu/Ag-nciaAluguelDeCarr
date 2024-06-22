from app.repositorys.base_repository import BaseRepository
from app.models.reserva_model import Reserva

class ReservaRepository(BaseRepository):
    def __init__(self):
        super().__init__(Reserva)

    def get_by_cliente_id(self, cliente_id):
        return Reserva.query.filter_by(cliente_id=cliente_id).all()

    def get_by_veiculo_id(self, veiculo_id):
        return Reserva.query.filter_by(veiculo_id=veiculo_id).all()
