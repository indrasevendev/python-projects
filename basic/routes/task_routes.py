from flask import Blueprint, request, jsonify
from ..database import db
from ..models.task import Task
from flask_jwt_extended import jwt_required

task_bp = Blueprint("tasks", __name__)

@task_bp.route("/tasks", methods=["GET"])
@jwt_required()
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

@task_bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    new_task = Task(title=data["title"])
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201


@task_bp.route("/tasks/<int:task_id>", methods=["PUT"])
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.done = not task.done
    db.session.commit()
    return jsonify(task.to_dict())


@task_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"})
