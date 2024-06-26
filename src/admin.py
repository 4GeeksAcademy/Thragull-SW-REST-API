import os
from flask_admin import Admin
from models import db, Country, City, User, Planets, Starships, Characters,Starship_Crew , Favourite_Planets, Favourite_Starships, Favourite_Characters
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'united'
    admin = Admin(app, name='Thragull Admin', template_mode='bootstrap3')

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(Country, db.session))
    admin.add_view(ModelView(City, db.session))
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Planets, db.session))
    admin.add_view(ModelView(Starships, db.session))
    admin.add_view(ModelView(Characters, db.session))
    admin.add_view(ModelView(Starship_Crew, db.session))
    admin.add_view(ModelView(Favourite_Planets, db.session))
    admin.add_view(ModelView(Favourite_Starships, db.session))
    admin.add_view(ModelView(Favourite_Characters, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))