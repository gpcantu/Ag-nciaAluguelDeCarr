from flask import jsonify, request

from app.services.feedback_service import FeedbackService

feedback_service = FeedbackService()


def get_all():
    feedbacks = feedback_service.fetch_all()
    return jsonify(feedbacks)


def get_by_id(feedback_id):
    feedback = feedback_service.fetch_by_id(feedback_id)
    if isinstance(feedback, dict):
        return jsonify(feedback)
    return feedback


def get_by_cliente_id(cliente_id):
    feedbacks = feedback_service.fetch_by_cliente_id(cliente_id)
    return jsonify(feedbacks)


def create():
    data = request.get_json()
    feedback = feedback_service.create(data)
    if isinstance(feedback, dict):
        return jsonify(feedback), 201  
    return feedback


def update(feedback_id):
    data = request.get_json()
    feedback = feedback_service.update(feedback_id, data)
    if isinstance(feedback, dict):
        return jsonify(feedback)
    return feedback


def delete(feedback_id):
    result = feedback_service.delete(feedback_id)
    if result:
        return '', 204 
    return jsonify({'error': 'Feedback não encontrado'}), 404