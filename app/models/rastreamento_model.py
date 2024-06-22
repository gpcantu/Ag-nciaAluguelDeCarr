from app.extentions import db

class Rastreamento(db.Model):
    __tablename__ = 'rastreamentos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    veiculo_id = db.Column(db.Integer, db.ForeignKey('veiculos.id'), nullable=False)
    data_hora = db.Column(db.Date, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    veiculo = db.relationship('Veiculo', back_populates='rastreamentos')
