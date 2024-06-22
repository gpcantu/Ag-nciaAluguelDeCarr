from app.repositorys.base_repository import BaseRepository
from app.models.seguro_model import Seguro

class SeguroRepository(BaseRepository):
    def __init__(self):
        super().__init__(Seguro)

    def get_by_tipo(self, tipo):
        return Seguro.query.filter_by(tipo=tipo).first()
