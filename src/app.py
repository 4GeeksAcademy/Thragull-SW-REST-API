"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Country, City, User, Planets, Starships, Characters, Favourite_Planets, Favourite_Starships, Favourite_Characters
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_users():
    # SELECT * FROM "Users"

    users = db.session.query(User, City, Country).select_from(User).join(City).join(Country).all()
    users_serialized = []
    for user, city, country in users:
        user_details=user.serialize()
        user_details['city']= city.name
        user_details['country']= country.name
        users_serialized.append(user_details)

    response_body = {
        "msg": "OK",
        "response": users_serialized
    }

    return jsonify(response_body), 200

@app.route('/user/favourites', methods=['GET'])
def get_user_favourites():
    # SELECT * FROM "Users"

    body= request.get_json(silent=True)
    if body is None:
        return jsonify({'msg': 'Body must have user info'}), 400
    if 'user_id' not in body:
        return jsonify({'msg': 'user_id field must be in body'}), 400
    user = User.query.get(body['user_id'])
    if user is None:
        return jsonify({'msg': 'User with id {} does not exist'.format(body['user_id'])}), 404
    
    favourite_planets = db.session.query(Favourite_Planets, Planets).join(Planets).filter(Favourite_Planets.user_id == body['user_id']).all()
    favourite_planets_serialized = []
    for favourite, planet in favourite_planets:
        favourite_planets_serialized.append({'favourite_planet_id': favourite.id, 'favourite_planet': planet.serialize()})
    
    favourite_characters = db.session.query(Favourite_Characters, Characters).join(Characters).filter(Favourite_Characters.user_id == body['user_id']).all()
    favourite_characters_serialized = []
    for favourite, character in favourite_characters:
        favourite_characters_serialized.append({'favourite_character_id': favourite.id, 'favourite_character': character.serialize()})

    favourite_starships = db.session.query(Favourite_Starships, Starships).join(Starships).filter(Favourite_Starships.user_id == body['user_id']).all()
    favourite_starships_serialized = []
    for favourite, starship in favourite_starships:
        favourite_starships_serialized.append({'favourite_starship_id': favourite.id, 'favourite_starship': starship.serialize()})
    
    response_body = {
        "msg": "OK",
        "favourite_planets": favourite_planets_serialized,
        "favourite_characters": favourite_characters_serialized,
        "favourite_starships": favourite_starships_serialized
    }

    return jsonify(response_body), 200

@app.route('/planets', methods=['GET'])
def get_planets():
    # SELECT * FROM "Planets"

    planets = Planets.query.all()
    planets_serialized = list(map(lambda planet: planet.serialize(), planets))
    response_body = {
        "msg": "OK",
        "response": planets_serialized
    }

    return jsonify(response_body), 200

@app.route('/planet/<int:id>', methods=['GET'])
def get_planet_by_id(id):
    # SELECT * FROM planets WHERE id = {planet_id};

    planet = Planets.query.get(id)
    response_body = {
        "msg": "OK",
        "response": planet.serialize()
    }

    return jsonify(response_body), 200

@app.route('/starships', methods=['GET'])
def get_starships():
    # SELECT * FROM "Starships"

    starships = Starships.query.all()
    starships_serialized = list(map(lambda starship: starship.serialize(), starships))
    response_body = {
        "msg": "OK",
        "response": starships_serialized
    }

    return jsonify(response_body), 200

@app.route('/starship/<int:id>', methods=['GET'])
def get_starship_by_id(id):
    # SELECT * FROM starships WHERE id = {starship_id};

    starship = Starships.query.get(id)
    response_body = {
        "msg": "OK",
        "response": starship.serialize()
    }

    return jsonify(response_body), 200

@app.route('/characters', methods=['GET'])
def get_characters():
    # SELECT * FROM "Characters"

    characters = Characters.query.all()
    characters_serialized = list(map(lambda character: character.serialize(), characters))
    response_body = {
        "msg": "OK",
        "response": characters_serialized
    }

    return jsonify(response_body), 200

@app.route('/character/<int:id>', methods=['GET'])
def get_character_by_id(id):
    # SELECT * FROM characters WHERE id = {character_id};

    character = Characters.query.get(id)
    response_body = {
        "msg": "OK",
        "response": character.serialize()
    }

    return jsonify(response_body), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
