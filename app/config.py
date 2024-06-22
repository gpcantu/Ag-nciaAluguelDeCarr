import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///{}'.format(os.path.join(os.getcwd(), 'aluguel_carros.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '1546'