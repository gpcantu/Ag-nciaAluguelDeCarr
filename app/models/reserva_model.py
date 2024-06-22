from app.extentions import db

class Reserva(db.Model):
    __tablename__ = 'reservas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    veiculo_id = db.Column(db.Integer, db.ForeignKey('veiculos.id'), nullable=False)
    data_inicio = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=False)
    valor_total = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)

    cliente = db.relationship('Cliente', back_populates='reservas')
    veiculo = db.relationship('Veiculo', back_populates='reservas')
    contrato = db.relationship('Contrato', uselist=False, back_populates='reserva')
    pagamento = db.relationship('Pagamento', uselist=False, back_populates='reserva')
    feedbacks = db.relationship('Feedback', back_populates='reserva')
