from app.extentions import db

class Pagamento(db.Model):
    __tablename__ = 'pagamentos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reserva_id = db.Column(db.Integer, db.ForeignKey('reservas.id'), nullable=False)
    valor_pago = db.Column(db.Float, nullable=False)
    data_pagamento = db.Column(db.Date, nullable=False)
    metodo_pagamento = db.Column(db.String(50), nullable=False)

    reserva = db.relationship('Reserva', back_populates='pagamento')
