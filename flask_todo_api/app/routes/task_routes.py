from flask import Blueprint, request, jsonify
from ..database import db
from ..models.task import Task
from flask_jwt_extended import jwt_required, get_jwt_identity

task_bp = Blueprint("tasks", __name__)

@task_bp.route("/tasks", methods=["POST"])
@jwt_required()
def create_task():
    current_user = get_jwt_identity()
    data = request.get_json()

    new_task = Task(
        title=data["title"],
        user_id=current_user
    )

    db.session.add(new_task)
    db.session.commit()

    return jsonify(new_task.to_dict()), 201

@task_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
@jwt_required()
def delete_task(task_id):
    current_user = get_jwt_identity()

    task = Task.query.get(task_id)

    if not task:
        return jsonify({"message": "Task not found"}), 404

    if str(task.user_id) != str(current_user):
        return jsonify({"message": "Forbidden"}), 403

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Task deleted"}), 200
