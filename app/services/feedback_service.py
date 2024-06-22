from app.repositorys.feedback_repository import FeedbackRepository
from flask import jsonify

class FeedbackService:
    def __init__(self):
        self.repository = FeedbackRepository()

    def to_dict(self, feedback):
        return {
            'id': feedback.id,
            'cliente_id': feedback.cliente_id,
            'reserva_id': feedback.reserva_id,
            'nota': feedback.nota,
            'comentario': feedback.comentario,
        }

    def error_response(self, message, status_code):
        response = jsonify({'error': message})
        response.status_code = status_code
        return response

    def fetch_all(self):
        feedbacks = self.repository.get_all()
        return [self.to_dict(feedback) for feedback in feedbacks]

    def fetch_by_id(self, feedback_id):
        feedback = self.repository.get_by_id(feedback_id)
        if feedback is None:
            return self.error_response("Feedback não encontrado", 404)
        return self.to_dict(feedback)

    def fetch_by_cliente_id(self, cliente_id):
        feedbacks = self.repository.get_by_cliente_id(cliente_id)
        return [self.to_dict(feedback) for feedback in feedbacks]

    def fetch_by_reserva_id(self, reserva_id):
        feedbacks = self.repository.get_by_reserva_id(reserva_id)
        return [self.to_dict(feedback) for feedback in feedbacks]

    def create(self, data):
        cliente_id = data.get('cliente_id')
        reserva_id = data.get('reserva_id')
        nota = data.get('nota')
        comentario = data.get('comentario')

        if not cliente_id or not reserva_id or not nota or not comentario:
            return self.error_response("Todos os campos são obrigatórios", 400)

        instance = self.repository.create(
            cliente_id=cliente_id,
            reserva_id=reserva_id,
            nota=nota,
            comentario=comentario
        )
        return self.to_dict(instance)

    def update(self, feedback_id, data):
        feedback = self.repository.get_by_id(feedback_id)
        if feedback is None:
            return self.error_response("Feedback não encontrado", 404)
        
        cliente_id = data.get('cliente_id')
        reserva_id = data.get('reserva_id')
        nota = data.get('nota')
        comentario = data.get('comentario')

        if not cliente_id or not reserva_id or not nota or not comentario:
            return self.error_response("Todos os campos são obrigatórios", 400)

        feedback = self.repository.update(
            feedback,
            cliente_id=cliente_id,
            reserva_id=reserva_id,
            nota=nota,
            comentario=comentario
        )
        return self.to_dict(feedback)

    def delete(self, feedback_id):
        feedback = self.repository.get_by_id(feedback_id)
        if feedback is None:
            return self.error_response("Feedback não encontrado", 404)
        self.repository.delete(feedback)
        return jsonify({'message': 'Feedback excluído com sucesso'}), 200