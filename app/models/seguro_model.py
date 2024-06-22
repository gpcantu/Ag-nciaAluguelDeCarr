from app.extentions import db

class Seguro(db.Model):
    __tablename__ = 'seguros'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo = db.Column(db.String(50), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.Text, nullable=False)
