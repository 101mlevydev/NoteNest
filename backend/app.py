from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/note_nest'
mongo = PyMongo(app)

# Define endpoints for CRUD operations on notes
@app.route('/notes', methods=['GET'])
def get_notes():
    notes = list(mongo.db.notes.find())
    return jsonify(notes), 200

@app.route('/notes', methods=['POST'])
def create_note():
    data = request.json
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    note_id = mongo.db.notes.insert_one(data).inserted_id
    return jsonify({'message': 'Note created successfully', 'note_id': str(note_id)}), 201

@app.route('/notes/<note_id>', methods=['GET'])
def get_note(note_id):
    note = mongo.db.notes.find_one({'_id': ObjectId(note_id)})
    if note:
        return jsonify(note), 200
    else:
        return jsonify({'error': 'Note not found'}), 404

@app.route('/notes/<note_id>', methods=['PUT'])
def update_note(note_id):
    data = request.json
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    result = mongo.db.notes.update_one({'_id': ObjectId(note_id)}, {'$set': data})
    if result.modified_count:
        return jsonify({'message': 'Note updated successfully'}), 200
    else:
        return jsonify({'error': 'Note not found'}), 404

@app.route('/notes/<note_id>', methods=['DELETE'])
def delete_note(note_id):
    result = mongo.db.notes.delete_one({'_id': ObjectId(note_id)})
    if result.deleted_count:
        return jsonify({'message': 'Note deleted successfully'}), 200
    else:
        return jsonify({'error': 'Note not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
