from app.extentions import db 

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    carteira_motorista = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(15), nullable=False)

    reservas = db.relationship('Reserva', back_populates='cliente')
    feedbacks = db.relationship('Feedback', back_populates='cliente')
