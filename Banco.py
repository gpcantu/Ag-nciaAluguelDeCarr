"""
Este módulo define a estrutura do banco de dados para uma agência de aluguel de carros.
Utiliza SQLAlchemy para mapear as tabelas do banco de dados e definir as relações entre elas.
"""

from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, Text, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker


Base = declarative_base()

class Cliente(Base):
    """Classe que representa um cliente."""
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    carteira_motorista = Column(String(20), unique=True, nullable=False)
    email = Column(String(100), nullable=False)
    telefone = Column(String(15), nullable=False)

    reservas = relationship('Reserva', back_populates='clientes')
    feedbacks = relationship('Feedback', back_populates='clientes')

class Veiculo(Base):
    """Classe que representa um veículo."""
    __tablename__ = 'veiculos'

    id = Column(Integer, primary_key=True)
    marca = Column(String(50), nullable=False)
    modelo = Column(String(50), nullable=False)
    ano = Column(Integer, nullable=False)
    placa = Column(String(10), unique=True, nullable=False)
    quilometragem = Column(Float, nullable=False)

    reservas = relationship('Reserva', back_populates='veiculos')
    manutencoes = relationship('Manutencao', back_populates='veiculos')
    rastreamentos = relationship('Rastreamento', back_populates='veiculos')

class Reserva(Base):
    """Classe que representa uma reserva de veículo."""
    __tablename__ = 'reservas'

    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    veiculo_id = Column(Integer, ForeignKey('veiculos.id'), nullable=False)
    data_inicio = Column(Date, nullable=False)
    data_fim = Column(Date, nullable=False)
    valor_total = Column(Float, nullable=False)
    status = Column(String(20), nullable=False)

    cliente = relationship('Cliente', back_populates='reservas')
    veiculo = relationship('Veiculo', back_populates='reservas')
    contrato = relationship('Contrato', uselist=False, back_populates='reservas')
    pagamento = relationship('Pagamento', uselist=False, back_populates='reservas')
    feedbacks = relationship('Feedback', back_populates='reservas')

class Manutencao(Base):
    """Classe que representa uma manutenção de veículo."""
    __tablename__ = 'manutencoes'

    id = Column(Integer, primary_key=True)
    veiculo_id = Column(Integer, ForeignKey('veiculos.id'), nullable=False)
    data_servico = Column(Date, nullable=False)
    quilometragem = Column(Float, nullable=False)
    descricao = Column(Text, nullable=False)

    veiculo = relationship('Veiculo', back_populates='manutencoes')

class Feedback(Base):
    """Classe que representa um feedback de cliente."""
    __tablename__ = 'feedbacks'

    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    reserva_id = Column(Integer, ForeignKey('reservas.id'), nullable=False)
    nota = Column(Integer, nullable=False)
    comentario = Column(Text, nullable=False)

    cliente = relationship('Cliente', back_populates='feedbacks')
    reserva = relationship('Reserva', back_populates='feedbacks')

class Seguro(Base):
    """Classe que representa um tipo de seguro."""
    __tablename__ = 'seguros'

    id = Column(Integer, primary_key=True)
    tipo = Column(String(50), nullable=False)
    valor = Column(Float, nullable=False)
    descricao = Column(Text, nullable=False)

class Contrato(Base):
    """Classe que representa um contrato de aluguel."""
    __tablename__ = 'contratos'

    id = Column(Integer, primary_key=True)
    reserva_id = Column(Integer, ForeignKey('reservas.id'), nullable=False)
    termos_condicoes = Column(Text, nullable=False)

    reserva = relationship('Reserva', back_populates='contratos')

class Pagamento(Base):
    """Classe que representa um pagamento."""
    __tablename__ = 'pagamentos'

    id = Column(Integer, primary_key=True)
    reserva_id = Column(Integer, ForeignKey('reservas.id'), nullable=False)
    valor_pago = Column(Float, nullable=False)
    data_pagamento = Column(Date, nullable=False)
    metodo_pagamento = Column(String(50), nullable=False)

    reserva = relationship('Reserva', back_populates='pagamentos')

class Rastreamento(Base):
    """Classe que representa um rastreamento de veículo."""
    __tablename__ = 'rastreamentos'

    id = Column(Integer, primary_key=True)
    veiculo_id = Column(Integer, ForeignKey('veiculos.id'), nullable=False)
    data_hora = Column(Date, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    veiculo = relationship('Veiculo', back_populates='rastreamentos')

# Configurando o banco de dados
engine = create_engine('sqlite:///aluguel_carros.db')
Base.metadata.create_all(engine)

# Criando uma sessão
Session = sessionmaker(bind=engine)
session = Session()
