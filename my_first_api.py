from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route('/greet/<first_name>', methods=['GET'])
def greet(first_name):
    # Return a greeting message with the provided name
    return jsonify({'message': f'Hello, {first_name}!'})

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
     
    return jsonify(users[user_id])

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = data.get('id')
    user_name = data.get('name')

    if user_id is None or user_name is None:
        return jsonify({'error': 'Both id and name are required'}), 400

    users[user_id] = user_name
    return jsonify({'message': f'User {user_name} added successfully'}), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    new_name = data.get('name')

    if new_name is None:
        return jsonify({'error': 'Name is required'}), 400

    users[user_id] = new_name
    return jsonify({'message': f'User {user_id} updated successfully'}), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404

    del users[user_id]
    return jsonify({'message': f'User {user_id} deleted successfully'}), 200

app.run(host='0.0.0.0', port='5000')
