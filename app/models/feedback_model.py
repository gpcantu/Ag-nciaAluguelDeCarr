from app.extentions import db

class Feedback(db.Model):
    __tablename__ = 'feedbacks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    reserva_id = db.Column(db.Integer, db.ForeignKey('reservas.id'), nullable=False)
    nota = db.Column(db.Integer, nullable=False)
    comentario = db.Column(db.Text, nullable=False)

    cliente = db.relationship('Cliente', back_populates='feedbacks')
    reserva = db.relationship('Reserva', back_populates='feedbacks')
