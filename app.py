from flask import Flask
from flask_pymongo import PyMongo
import datetime

app = Flask(__name__)
app.config['MONGO_URI'] = ''
app.config['SECRET_KEY'] = ''

mongo = PyMongo(app)

# Import routes to register them with the Flask app
from routes.todo_routes import *

if __name__ == '__main__':
    app.run(debug=True)
