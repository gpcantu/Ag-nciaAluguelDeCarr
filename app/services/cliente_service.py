from app.repositorys.cliente_repository import ClienteRepository
from flask import jsonify

class ClienteService:
    def __init__(self):
        self.repository = ClienteRepository()

    def to_dict(self, cliente):
        return {
            'id': cliente.id,
            'nome': cliente.nome,
            'cpf': cliente.cpf,
            'carteira_motorista': cliente.carteira_motorista,
            'email': cliente.email,
            'telefone': cliente.telefone
        }

    def error_response(self, message, status_code):
        response = jsonify({'error': message})
        response.status_code = status_code
        return response

    def create(self, data):
        nome = data.get('nome')
        cpf = data.get('cpf')
        carteira_motorista = data.get('carteira_motorista')
        email = data.get('email')
        telefone = data.get('telefone')

        if not nome or not cpf or not carteira_motorista or not email or not telefone:
            return self.error_response("Todos os campos são obrigatórios", 400)

        instance = self.repository.create(
            nome=nome,
            cpf=cpf,
            carteira_motorista=carteira_motorista,
            email=email,
            telefone=telefone
        )
        return self.to_dict(instance)

    def update(self, cliente_id, data):
        cliente = self.repository.get_by_id(cliente_id)
        if cliente is None:
            return self.error_response("Cliente não encontrado", 404)
        
        nome = data.get('nome')
        cpf = data.get('cpf')
        carteira_motorista = data.get('carteira_motorista')
        email = data.get('email')
        telefone = data.get('telefone')

        if not nome or not cpf or not carteira_motorista or not email or not telefone:
            return self.error_response("Todos os campos são obrigatórios", 400)

        cliente = self.repository.update(
            cliente,
            nome=nome,
            cpf=cpf,
            carteira_motorista=carteira_motorista,
            email=email,
            telefone=telefone
        )
        return self.to_dict(cliente)

    def fetch_by_id(self, cliente_id):
        cliente = self.repository.get_by_id(cliente_id)
        if cliente is None:
            return self.error_response("Cliente não encontrado", 404)
        return self.to_dict(cliente)

    def delete(self, cliente_id):
        cliente = self.repository.get_by_id(cliente_id)
        if cliente is None:
            return self.error_response("Cliente não encontrado", 404)
        self.repository.delete(cliente)
        return jsonify({'message': 'Cliente excluído com sucesso'}), 200

    def fetch_all(self):
        clientes = self.repository.get_all()
        return [self.to_dict(cliente) for cliente in clientes]

    def fetch_by_cpf(self, cpf):
        cliente = self.repository.get_by_cpf(cpf)
        if cliente is None:
            return self.error_response("Cliente não encontrado", 404)
        return self.to_dict(cliente)

    def fetch_by_nome(self, nome):
        clientes = self.repository.get_by_nome(nome)
        if not clientes:
            return self.error_response("Cliente não encontrado", 404)
        return [self.to_dict(cliente) for cliente in clientes]

    def fetch_by_email(self, email):
        cliente = self.repository.get_by_email(email)
        if cliente is None:
            return self.error_response("Cliente não encontrado", 404)
        return self.to_dict(cliente)
