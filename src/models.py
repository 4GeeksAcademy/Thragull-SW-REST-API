from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()

class Country(db.Model):
    __tablename__ = 'country'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return f'Country: {self.name}'
    
    def serialize(self):
        return {
            "id": self.id,
            "country": self.name,
        }

class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    country= db.relationship(Country)
    
    def __repr__(self):
        return f'City {self.name} from {self.country}'
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "country": self.country_id
        }

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    country= db.relationship(Country)
    address = db.Column(db.String(250), nullable=False)
    address2 = db.Column(db.String(250))
    address3 = db.Column(db.String(250))
    zipcode = db.Column(db.Integer, nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    city = db.relationship(City)
    phone = db.Column(db.Integer, nullable=False)
    registered = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    is_active = db.Column(db.Boolean(), unique=False, nullable=False, default=True)

    def __repr__(self):
        return f'User: {self.username} with name: {self.name} {self.surname}'

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "country": self.country_id,
            "address": self.address,
            "address2": self.address2,
            "address3": self.address3,
            "zipcode": self.zipcode,
            "city": self.city_id,
            "phone": self.phone,
            "registered": self.registered,
            "is_active": self.is_active
            # do not serialize the password, its a security breach
        }
    
class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    population = db.Column(db.BigInteger, nullable=False)
    area = db.Column(db.Integer, nullable=False)
    suns =  db.Column(db.Integer)
    moons = db.Column(db.Integer)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False, default=True)

    def __repr__(self):
        return f'Planet: {self.name}'
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "area": self.area,
            "suns": self.suns,
            "moons": self.moons,
            "is_active": self.is_active
        }
    
class Starships(db.Model):
    __tablename__ = 'starships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    crew_capacity = db.Column(db.Integer, nullable=False)
    length = db.Column(db.Float, nullable=False)
    width =  db.Column(db.Float, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False, default=True)

    def __repr__(self):
        return f'Starship: {self.name}'
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "crew_capacity": self.crew_capacity,
            "length": self.length,
            "width": self.width,
            "is_active": self.is_active
        }

class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'), unique=True, nullable=False)
    planet= db.relationship(Planets)
    commands_id = db.Column(db.Integer, db.ForeignKey('starships.id'), unique=True)
    commands = db.relationship(Starships)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False, default=True)

    def __repr__(self):
        return f'Character: {self.name}'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "weight": self.weight,
            "planet": self.planet_id,
            "commands": self.commands_id,
            "is_active": self.is_active
        }

class Starship_Crew(db.Model):
    __tablename__ = 'starship_crew'
    id = db.Column(db.Integer, primary_key=True)
    starship_id = db.Column(db.Integer, db.ForeignKey('starships.id'), nullable=False)
    starship = db.relationship(Starships)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=False)
    character = db.relationship(Characters)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False, default=True)

    def __repr__(self):
        return f'{self.character} is part of the crew in the Starship {self.starship}'

    def serialize(self):
        return {
            "id": self.id,
            "starship": self.starship_id,
            "character": self.character_id,
            "is_active": self.is_active
        }


class Favourite_Characters(db.Model):
    __tablename__ = 'favourite_characters'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship(User)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=False)
    character = db.relationship(Characters)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False, default=True)

    def __repr__(self):
        return f'Favourite {self.character} from {self.user}'

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user_id,
            "character": self.character_id,
            "is_active": self.is_active
        }

class Favourite_Starships(db.Model):
    __tablename__ = 'favourite_starships'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship(User)
    starship_id = db.Column(db.Integer, db.ForeignKey('starships.id'), nullable=False)
    starship = db.relationship(Starships)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False, default=True)

    def __repr__(self):
        return f'Favourite {self.starship} from {self.user}'

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user_id,
            "starship": self.starship_id,
            "is:active": self.is_active
        }

class Favourite_Planets(db.Model):
    __tablename__ = 'favourite_planets'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship(User)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=False)
    planet = db.relationship(Planets)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False, default=True)

    def __repr__(self):
        return f'Favourite {self.planet} from {self.user}'

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user_id,
            "planet": self.planet_id,
            "is_active": self.is_active
        }