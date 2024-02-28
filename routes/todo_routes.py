from flask import request, jsonify
from bson import ObjectId
from middleware.jwt_validation import token_required
from app import app, mongo, datetime  
import jwt
from models.todo_schema import TodoItem

@app.route('/login', methods=['POST'])
def login():
    try:
        auth = request.get_json()
        if auth and 'username' in auth and 'password' in auth:
            if auth['username'] == 'test@123' and auth['password'] == '12345':
                token = jwt.encode({'user': auth['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                                   app.config['SECRET_KEY'], algorithm="HS256")
                return jsonify({'token': token})
            else:
                return jsonify({'message': 'Invalid username or password'}), 401
        else:
            return jsonify({'message': 'Invalid request format'}), 400
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500


@app.route('/todo', methods=['GET'])
@token_required
def get_all_todos():
    try:
        todos = mongo.db.todo.find({})
        output = []
        for todo in todos:
            output.append({'id': str(todo['_id']), 'name': todo['name'], 'description': todo['description']})
        return jsonify({'todos': output})
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500


@app.route('/todo/<id>', methods=['GET'])
@token_required
def get_todo(id):
    try:
        todo = mongo.db.todo.find_one({'_id': ObjectId(id)})
        if todo:
            return jsonify({'id': str(todo['_id']), 'name': todo['name'], 'description': todo['description']})
        else:
            return jsonify({'message': 'Todo not found'}), 404
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500


@app.route('/todo', methods=['POST'])
@token_required
def create_todo():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'message': 'Request data is missing or not in JSON format'}), 400

        name = data.get('name')
        description = data.get('description')

        if not name or not description:
            return jsonify({'message': 'Name or description is missing in the request data'}), 400
   
        # Create a new Todo document using the schema
        new_todo = TodoItem(
            name=name,
            description=description,
            created_at=datetime.datetime.utcnow()
        )
        new_todo.save()  # Save the new Todo document to the database

        # Return a response with the details of the newly created Todo item
        return jsonify({'id': str(new_todo.id), 'name': new_todo.name, 'description': new_todo.description}), 201

    except Exception as e:
        return jsonify({'message': 'An error occurred while creating todo item', 'error': str(e)}), 500

@app.route('/todo/<id>', methods=['PUT'])
@token_required
def update_todo(id):
    try:
        data = request.get_json()
        if 'name' in data and 'description' in data:
            name = data['name']
            description = data['description']

            # Update the todo item identified by the provided id
            todo_item = TodoItem.objects(id=ObjectId(id)).first()
            if todo_item:
                todo_item.name = name
                todo_item.description = description
                todo_item.save()
                return jsonify({'message': 'ToDo item updated!'}), 200
            else:
                return jsonify({'message': 'Todo item not found'}), 404
        else:
            return jsonify({'message': 'Missing required fields in request data'}), 400
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500


@app.route('/todo/<id>', methods=['DELETE'])
@token_required
def delete_todo(id):
    try:
        todo_item = TodoItem.objects(id=ObjectId(id)).first()
        if todo_item:
            todo_item.delete()
            return jsonify({'message': 'ToDo item deleted!'})
        else:
            return jsonify({'message': 'ToDo item not found!'}), 404
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500