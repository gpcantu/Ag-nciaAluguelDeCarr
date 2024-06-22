from app.extentions import db

class Contrato(db.Model):
    __tablename__ = 'contratos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reserva_id = db.Column(db.Integer, db.ForeignKey('reservas.id'), nullable=False)
    termos_condicoes = db.Column(db.Text, nullable=False)

    reserva = db.relationship('Reserva', back_populates='contrato')
