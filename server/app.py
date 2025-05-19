# server/app.py

from flask import Flask
from flask_migrate import Migrate
from flask import jsonify
from models import Pet
from models import db

# create a Flask application instance 
app = Flask(__name__)

# configure the database connection to the local file app.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# configure flag to disable modification tracking and use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create a Migrate object to manage schema modifications
migrate = Migrate(app, db)

# initialize the Flask application to use the database
db.init_app(app)

@app.route('/')
def home():
    return "Welcome to the Flask app!"

@app.route('/pets')
def get_pets():
    pets = Pet.query.all()  # fetch all pets from database
    pets_list = [{"id": pet.id, "name": pet.name, "species": pet.species} for pet in pets]
    return jsonify(pets_list)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
