from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config  

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import (cliente_route, contrato_route, feedback_route, manutencao_route, pagamento_route, rastreamento_route, reserva_route, seguro_route, veiculo_route)
    
    app.register_blueprint(cliente_route.cliente_bp)
    app.register_blueprint(contrato_route.contrato_bp)
    app.register_blueprint(feedback_route.feedback_bp)
    app.register_blueprint(manutencao_route.manutencao_bp)
    app.register_blueprint(pagamento_route.pagamento_bp)
    app.register_blueprint(rastreamento_route.rastreamento_bp)
    app.register_blueprint(reserva_route.reserva_bp)
    app.register_blueprint(seguro_route.seguro_bp)
    app.register_blueprint(veiculo_route.veiculo_bp)

    return app
