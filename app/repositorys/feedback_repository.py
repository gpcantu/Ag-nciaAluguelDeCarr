from app.repositorys.base_repository import BaseRepository
from app.models.feedback_model import Feedback

class FeedbackRepository(BaseRepository):
    def __init__(self):
        super().__init__(Feedback)

    def get_by_cliente_id(self, cliente_id):
        return Feedback.query.filter_by(cliente_id=cliente_id).all()

    def get_by_reserva_id(self, reserva_id):
        return Feedback.query.filter_by(reserva_id=reserva_id).all()
