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
from dbfiller import insert_countries, insert_worldwide_cities, insert_planets, insert_starships, insert_characters

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
        if user_details['is_active']:
            users_serialized.append(user_details)

    response_body = {
        "msg": "OK",
        "response": users_serialized
    }

    return jsonify(response_body), 200

@app.route('/user', methods=['POST'])
def add_user():
    body = request.get_json(silent=True)
    if body is  None:
        return jsonify({'msg':'Body must contain something'}), 400
    if ('username' not in body or 
    'name' not in body or 
    'surname' not in body or 
    'email' not in body or 
    'password' not in body or 
    'address' not in body or 
    'country_id' not in body or 
    'city_id' not in body or 
    'zipcode' not in body or 
    'phone' not in body):
        return jsonify({'msg': 'One of the following fields is missing: Username, name, surname, email, password, address, country_id, city_id, zipcode or phone'}), 400
    country_exist_in_db = Country.query.filter_by(id=body['country_id']).first()
    if not country_exist_in_db:
        return jsonify({'msg': 'The country id {} does not exist in this database'.format(body['country_id'])}), 400
    city_exist_in_db = City.query.filter_by(id=body['city_id']).first()
    if not city_exist_in_db:
        return jsonify({'msg': 'The city id {} does not exist in this database'.format(body['city_id'])}), 400
    user = User()
    user.username= body['username']
    user.name= body['name']
    user.surname= body['surname']
    user.email= body['email']
    user.password= body['password']
    user.address= body['address']
    if 'address2' in body:
        user.address2= body['address2']
    if 'address3' in body:
        user.address3= body['address3']
    user.country_id= body['country_id']
    user.city_id= body['city_id']
    user.zipcode= body['zipcode']
    user.phone= body['phone']

    db.session.add(user)
    db.session.commit()

    return jsonify({'msg': 'New user added'}), 201


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
        if favourite.serialize()['is_active']:
            favourite_planets_serialized.append({'favourite_planet_id': favourite.id, 'favourite_planet': planet.serialize()})
    
    favourite_characters = db.session.query(Favourite_Characters, Characters, Starships, Planets).select_from(Favourite_Characters).join(Characters).outerjoin(Starships).join(Planets).filter(Favourite_Characters.user_id == body['user_id']).all()
    favourite_characters_serialized = []
    for favourite, character, starship, planet in favourite_characters:
        if favourite.serialize()['is_active']:
            favourite_character= character.serialize()
            favourite_character['planet']=planet.name
            if favourite_character['commands'] is not None:
                favourite_character['commands']=starship.name
            favourite_characters_serialized.append({'favourite_character_id': favourite.id, 'favourite_character': favourite_character})

    favourite_starships = db.session.query(Favourite_Starships, Starships).join(Starships).filter(Favourite_Starships.user_id == body['user_id']).all()
    favourite_starships_serialized = []
    for favourite, starship in favourite_starships:
        if favourite.serialize()['is_active']:
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
    if planet is None:
        return jsonify({'msg': 'Planet not found'})
    response_body = {
        "msg": "OK",
        "response": planet.serialize()
    }

    return jsonify(response_body), 200

@app.route('/planet', methods=['POST'])
def add_planet():
    body= request.get_json(silent=True)
    if body is None:
        return jsonify({'msg': 'The body must contain something'}), 400
    if ('name' not in body or
    'population' not in body or
    'area' not in body):
        return jsonify({'msg': 'One of the following fields is missing: name, population or area'}), 400
    planet=Planets()
    planet.name=body['name']
    planet.population=body['population']
    planet.area=body['area']
    if 'suns' in body:
        planet.suns=body['suns']
    if 'moons' in body:
        planet.moons=body['moons']
    
    db.session.add(planet)
    db.session.commit()

    return jsonify({'msg': 'Planet has been added'}), 201

@app.route('/planet/<int:id>', methods=['PUT'])
def modify_planet(id):
    body= request.get_json(silent=True)
    if body is None:
        return jsonify({'msg': 'The body must contain something'}), 400
    if ('name' not in body and
    'population' not in body and
    'area' not in body and
    'suns' not in body and
    'moons' not in body):
        return jsonify({'msg': 'You must specify at least one valid field to modify'}), 400
    planet=Planets().query.get(id)
    if planet is None:
        return jsonify({'msg': 'There is no planet with this ID'}), 404
    for key, value in body.items():
        if hasattr(planet, key):
            setattr(planet, key , value)
        else:
            return jsonify({'msg': 'Invalid Field: {}'.format(key)})
    
    db.session.commit()

    return jsonify({'msg': 'Planet has been succesfully modified'}), 200

@app.route('/planet/<int:id>', methods=['DELETE'])
def delete_planet(id):
    planet = Planets.query.get(id)
    if planet is None:
        return jsonify({'msg': 'The planet does not exist in database'}), 404
    db.session.delete(planet)
    db.session.commit()

    return jsonify({'msg': 'Planet deleted succesfully'}), 200

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

@app.route('/starship', methods=['POST'])
def add_starship():
    body= request.get_json(silent=True)
    if body is None:
        return jsonify({'msg': 'The body must contain something'}), 400
    if ('name' not in body or
    'model' not in body or
    'crew_capacity' not in body or
    'length' not in body or
    'width' not in body):
        return jsonify({'msg': 'One of the following fields is missing: name, model, crew_capacity, length or width'}), 400
    starship=Starships()
    starship.name=body['name']
    starship.model=body['model']
    starship.crew_capacity =body['crew_capacity']
    starship.length=body['length']
    starship.width=body['width']
    
    db.session.add(starship)
    db.session.commit()

    return jsonify({'msg': 'Starship has been added'}), 201

@app.route('/starship/<int:id>', methods=['PUT'])
def modify_starship(id):
    body= request.get_json(silent=True)
    if body is None:
        return jsonify({'msg': 'Body must contain something'}), 400
    if ('name' not in body and
    'model' not in body and
    'crew_capacity' not in body and
    'length' not in body and
    'width' not in body):
        return jsonify({'msg': 'You must specify at least one mandatory field'}), 400
    starship = Starships.query.get(id)
    if starship is None:
        return jsonify({'msg': 'There is no starship with this ID'}), 404
    for key, value in body.items():
        if hasattr(starship, key):
            setattr(starship, key, value)
        else:
            return jsonify({'msg': 'Invalid Field: {}'.format(key)}), 400
        
    db.session.commit()

    return jsonify({'msg': 'Starship succesfully modified'}), 200

@app.route('/starship/<int:id>', methods=['DELETE'])
def delete_starship(id):
    starship = Starships.query.get(id)
    if starship is None:
        return jsonify({'msg': 'There is no starship in Database with this ID'}), 404
    
    db.session.delete(starship)
    db.session.commit()

    return jsonify({'msg': 'Starship succesfully deleted'}), 200

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

@app.route('/character', methods=['POST'])
def post_character():
    body=request.get_json(silent=True)
    if body is None:
        return jsonify({'msg': 'Body must contain something'}), 400
    if ('name' not in body or
        'height' not in body or
        'weight' not in body):
        return jsonify({'msg': 'One or more of the mandatory fields are missing'}), 400
    character = Characters()
    for key, value in body.items():
        if hasattr(character, key):
            setattr(character, key, value)
        else:
            return jsonify({'msg': 'Invalid Field {}'.format(key)}), 400
    
    db.session.add(character)
    db.session.commit()

    return jsonify({'msg': 'New character succesfully added'}), 201

@app.route('/character/<int:id>', methods=['PUT'])
def modify_character(id):
    body= request.get_json(silent=True)
    if body is None:
        return jsonify({'msg': 'Body must contain something'}), 400
    if ('name' not in body and
        'height' not in body and
        'weight' not in body and
        'planet_id' not in body and
        'commands_id' not in body):
        return jsonify({'msg': 'You must specify at least one mandatory field'}), 400
    character = Characters.query.get(id)
    if character is None:
        return jsonify({'msg': 'There is no Character with this ID'}), 404
    for key, value in body.items():
        if hasattr(character, key):
            setattr(character, key, value)
        else:
            return jsonify({'msg': 'Invalid Field: {}'.format(key)}), 400
    
    db.session.commit()

    return jsonify({'msg': 'Character succesfully modified'}), 200

@app.route('/character/<int:id>', methods=['DELETE'])
def delete_character(id):
    character = Characters.query.get(id)
    if character is None:
        return jsonify({'msg': 'There is no character with this ID'}), 404
    
    db.session.delete(character)
    db.session.commit()

    return jsonify({'msg': 'Character succesfully deleted'}), 200

@app.route('/api/dbfiller', methods=['GET'])
def db_filler():
    #insert_countries()
    #insert_worldwide_cities()
    insert_planets()
    insert_starships()
    insert_characters()

    return jsonify({'msg': 'Everything is all right'})

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
