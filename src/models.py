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
            # do not serialize the password, its a security breach
        }

class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    country= db.relationship(Country)
    
    def __repr__(self):
        return f'City {self.name} from country {self.country_id}'
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False, unique=True)
    name = db.Column(db.String(25), nullable=False)
    surname = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(25), nullable=False)
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
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    population = db.Column(db.BigInteger, nullable=False)
    area = db.Column(db.Integer, nullable=False)
    suns =  db.Column(db.Integer)
    moons = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }
    
class Starships(db.Model):
    __tablename__ = 'starships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    crew_capacity = db.Column(db.Integer, nullable=False)
    length = db.Column(db.Integer, nullable=False)
    width =  db.Column(db.Integer, nullable=False)
    moons = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'), unique=True, nullable=False)
    planet= db.relationship(Planets)
    starship_id = db.Column(db.Integer, db.ForeignKey('starships.id'))
    starship = db.relationship(Starships, foreign_keys=[starship_id])
    commands_id = db.Column(db.Integer, db.ForeignKey('starships.id'), unique=True)
    commands = db.relationship(Starships, foreign_keys=[commands_id])

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
            # do not serialize the password, its a security breach
        }

class Favourite_Characters(db.Model):
    __tablename__ = 'favourite_characters'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship(User)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=False)
    character = db.relationship(Characters)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
        }

class Favourite_Starships(db.Model):
    __tablename__ = 'favourite_starships'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship(User)
    starship_id = db.Column(db.Integer, db.ForeignKey('starships.id'), nullable=False)
    starship = db.relationship(Starships)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
        }

class Favourite_Planets(db.Model):
    __tablename__ = 'favourite_planets'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship(User)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=False)
    planet = db.relationship(Planets)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
        }