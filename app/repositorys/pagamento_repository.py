from app.repositorys.base_repository import BaseRepository
from app.models.pagamento_model import Pagamento

class PagamentoRepository(BaseRepository):
    def __init__(self):
        super().__init__(Pagamento)

    def get_by_reserva_id(self, reserva_id):
        return Pagamento.query.filter_by(reserva_id=reserva_id).first()
