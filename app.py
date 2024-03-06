from flask import Flask
from flask_pymongo import PyMongo
import datetime

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://selva658:selva100_@cluster0.fowgx.mongodb.net/lybrate'
app.config['SECRET_KEY'] = 'EYMDyiQy4MtIQPcET-xV-yG1dNWGF1P0A9tiaYumN6EXtldIamagSfGgNQypmCq4'

mongo = PyMongo(app)

# Import routes to register them with the Flask app
from routes.todo_routes import *

if __name__ == '__main__':
    app.run(debug=True)
