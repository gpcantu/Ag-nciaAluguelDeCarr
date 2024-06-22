from app.extentions import db

class Manutencao(db.Model):
    __tablename__ = 'manutencoes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    veiculo_id = db.Column(db.Integer, db.ForeignKey('veiculos.id'), nullable=False)
    data_servico = db.Column(db.Date, nullable=False)
    quilometragem = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.Text, nullable=False)

    veiculo = db.relationship('Veiculo', back_populates='manutencoes')