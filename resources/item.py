from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

item_bp = Blueprint('item_bp', __name__)

@item_bp.route('/items', methods=['GET'])
@jwt_required()
def get_items():
    return jsonify([])

@item_bp.route('/items', methods=['POST'])
@jwt_required()
def create_item():
    data = request.get_json()
    return jsonify(data), 201

@item_bp.route('/items/<int:id>', methods=['PUT'])
@jwt_required()
def update_item(id):
    data = request.get_json()
    return jsonify(data)

@item_bp.route('/items/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_item(id):
    return jsonify({"message": f"Item {id} deleted"})