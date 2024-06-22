from app.repositorys.base_repository import BaseRepository
from app.models.cliente_model import Cliente

class ClienteRepository(BaseRepository):
    def __init__(self):
        super().__init__(Cliente)

    def get_by_cpf(self, cpf):
        return Cliente.query.filter_by(cpf=cpf).first()

    def get_by_email(self, email):
        return Cliente.query.filter_by(email=email).first()

    def get_by_nome(self, nome):
        return Cliente.query.filter_by(nome=nome).all()
