from mongoengine import Document, StringField, DateTimeField, ObjectIdField, connect
from app import app

# Connect to MongoDB database
connect('lybrate', host=app.config['MONGO_URI'] )

class TodoItem(Document):
    name = StringField(required=True, max_length=100)
    description = StringField(required=True)
    created_at = DateTimeField(required=True)

    meta = {'collection': 'todo'}

    def to_json(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at
        }
