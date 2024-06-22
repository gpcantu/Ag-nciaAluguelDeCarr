from app.extentions import db

class Veiculo(db.Model):
    __tablename__ = 'veiculos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    marca = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    placa = db.Column(db.String(10), unique=True, nullable=False)
    quilometragem = db.Column(db.Float, nullable=False)

    reservas = db.relationship('Reserva', back_populates='veiculo')
    manutencoes = db.relationship('Manutencao', back_populates='veiculo')
    rastreamentos = db.relationship('Rastreamento', back_populates='veiculo')
