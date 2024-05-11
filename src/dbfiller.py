from models import db, Country, City, Starship_Crew, Starships, Planets, Characters

countries = [
                "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria",
                "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia",
                "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon",
                "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo", "Costa Rica", "Croatia", "Cuba",
                "Cyprus", "Czech Republic", "Democratic Republic of the Congo", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor",
                "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France",
                "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti",
                "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", 
                "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya",
                "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania",
                "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru",
                "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia", "Norway", "Oman", "Pakistan",
                "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia",
                "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe",
                "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", 
                "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania",
                "Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates",
                "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
]

cities = [
    {"country": "Spain", "name": "Albacete"},
    {"country": "Spain", "name": "Ávila"},
    {"country": "Spain", "name": "Badajoz"},
    {"country": "Spain", "name": "Barcelona"},
    {"country": "Spain", "name": "Burgos"},
    {"country": "Spain", "name": "Cáceres"},
    {"country": "Spain", "name": "Cádiz"},
    {"country": "Spain", "name": "Castellón de la Plana"},
    {"country": "Spain", "name": "Ciudad Real"},
    {"country": "Spain", "name": "Córdoba"},
    {"country": "Spain", "name": "La Coruña"},
    {"country": "Spain", "name": "Cuenca"},
    {"country": "Spain", "name": "Gerona"},
    {"country": "Spain", "name": "Granada"},
    {"country": "Spain", "name": "Guadalajara"},
    {"country": "Spain", "name": "Huelva"},
    {"country": "Spain", "name": "Huesca"},
    {"country": "Spain", "name": "Jaén"},
    {"country": "Spain", "name": "León"},
    {"country": "Spain", "name": "Lérida"},
    {"country": "Spain", "name": "Logroño"},
    {"country": "Spain", "name": "Lugo"},
    {"country": "Spain", "name": "Madrid"},
    {"country": "Spain", "name": "Málaga"},
    {"country": "Spain", "name": "Murcia"},
    {"country": "Spain", "name": "Orense"},
    {"country": "Spain", "name": "Oviedo"},
    {"country": "Spain", "name": "Palencia"},
    {"country": "Spain", "name": "Las Palmas de Gran Canaria"},
    {"country": "Spain", "name": "Pontevedra"},
    {"country": "Spain", "name": "Salamanca"},
    {"country": "Spain", "name": "Santa Cruz de Tenerife"},
    {"country": "Spain", "name": "Santander"},
    {"country": "Spain", "name": "Segovia"},
    {"country": "Spain", "name": "Sevilla"},
    {"country": "Spain", "name": "Soria"},
    {"country": "Spain", "name": "Tarragona"},
    {"country": "Spain", "name": "Teruel"},
    {"country": "Spain", "name": "Toledo"},
    {"country": "Spain", "name": "Valencia"},
    {"country": "Spain", "name": "Valladolid"},
    {"country": "Spain", "name": "Vitoria-Gasteiz"},
    {"country": "Spain", "name": "Zamora"},
    {"country": "Spain", "name": "Zaragoza"},
    {"country": "France", "name": "Ajaccio"},
    {"country": "France", "name": "Amiens"},
    {"country": "France", "name": "Besançon"},
    {"country": "France", "name": "Bordeaux"},
    {"country": "France", "name": "Caen"},
    {"country": "France", "name": "Clermont-Ferrand"},
    {"country": "France", "name": "Dijon"},
    {"country": "France", "name": "Grenoble"},
    {"country": "France", "name": "Lille"},
    {"country": "France", "name": "Limoges"},
    {"country": "France", "name": "Lyon"},
    {"country": "France", "name": "Marseille"},
    {"country": "France", "name": "Metz"},
    {"country": "France", "name": "Montpellier"},
    {"country": "France", "name": "Nantes"},
    {"country": "France", "name": "Nice"},
    {"country": "France", "name": "Orleans"},
    {"country": "France", "name": "Paris"},
    {"country": "France", "name": "Pau"},
    {"country": "France", "name": "Rennes"},
    {"country": "France", "name": "Rouen"},
    {"country": "France", "name": "Strasbourg"},
    {"country": "France", "name": "Toulouse"},
    {"country": "France", "name": "Tours"},
    {"country": "Germany", "name": "Berlin"},
    {"country": "Germany", "name": "Bremen"},
    {"country": "Germany", "name": "Hamburg"},
    {"country": "Germany", "name": "Düsseldorf"},
    {"country": "Germany", "name": "Saarbrücken"},
    {"country": "Germany", "name": "Stuttgart"},
    {"country": "Germany", "name": "Mainz"},
    {"country": "Germany", "name": "Hannover"},
    {"country": "Germany", "name": "Potsdam"},
    {"country": "Germany", "name": "Schwerin"},
    {"country": "Germany", "name": "Wiesbaden"},
    {"country": "Germany", "name": "Kiel"},
    {"country": "Germany", "name": "Magdeburg"},
    {"country": "Germany", "name": "Dresden"},
    {"country": "Germany", "name": "Erfurt"},
    {"country": "Germany", "name": "Düsseldorf"},
    {"country": "Germany", "name": "Mainz"},
    {"country": "Germany", "name": "Munich"},
    {"country": "Germany", "name": "Potsdam"},
    {"country": "Germany", "name": "Hamburg"},
    {"country": "Afghanistan", "name": "Kabul"},
    {"country": "Albania", "name": "Tirana"},
    {"country": "United States", "name": "Montgomery"},
    {"country": "United States", "name": "Juneau"},
    {"country": "United States", "name": "Phoenix"},
    {"country": "United States", "name": "Little Rock"},
    {"country": "United States", "name": "Sacramento"},
    {"country": "United States", "name": "Denver"},
    {"country": "United States", "name": "Hartford"},
    {"country": "United States", "name": "Dover"},
    {"country": "United States", "name": "Tallahassee"},
    {"country": "United States", "name": "Atlanta"},
    {"country": "United States", "name": "Honolulu"},
    {"country": "United States", "name": "Boise"},
    {"country": "United States", "name": "Springfield"},
    {"country": "United States", "name": "Indianapolis"},
    {"country": "United States", "name": "Des Moines"},
    {"country": "United States", "name": "Topeka"},
    {"country": "United States", "name": "Frankfort"},
    {"country": "United States", "name": "Baton Rouge"},
    {"country": "United States", "name": "Augusta"},
    {"country": "United States", "name": "Annapolis"},
    {"country": "United States", "name": "Boston"},
    {"country": "United States", "name": "Lansing"},
    {"country": "United States", "name": "Saint Paul"},
    {"country": "United States", "name": "Jackson"},
    {"country": "United States", "name": "Jefferson City"},
    {"country": "United States", "name": "Helena"},
    {"country": "United States", "name": "Lincoln"},
    {"country": "United States", "name": "Carson City"},
    {"country": "United States", "name": "Concord"},
    {"country": "United States", "name": "Trenton"},
    {"country": "United States", "name": "Santa Fe"},
    {"country": "United States", "name": "Albany"},
    {"country": "United States", "name": "Raleigh"},
    {"country": "United States", "name": "Bismarck"},
    {"country": "United States", "name": "Columbus"},
    {"country": "United States", "name": "Oklahoma City"},
    {"country": "United States", "name": "Salem"},
    {"country": "United States", "name": "Harrisburg"},
    {"country": "United States", "name": "Providence"},
    {"country": "United States", "name": "Columbia"},
    {"country": "United States", "name": "Pierre"},
    {"country": "United States", "name": "Nashville"},
    {"country": "United States", "name": "Austin"},
    {"country": "United States", "name": "Salt Lake City"},
    {"country": "United States", "name": "Montpelier"},
    {"country": "United States", "name": "Richmond"},
    {"country": "United States", "name": "Olympia"},
    {"country": "United States", "name": "Charleston"},
    {"country": "United States", "name": "Madison"},
    {"country": "United States", "name": "Cheyenne"},
    {"country": "Italy", "name": "Roma"},
    {"country": "Italy", "name": "Milano"},
    {"country": "Italy", "name": "Napoli"},
    {"country": "Italy", "name": "Torino"},
    {"country": "Italy", "name": "Palermo"},
    {"country": "Italy", "name": "Genova"},
    {"country": "Italy", "name": "Bologna"},
    {"country": "Italy", "name": "Firenze"},
    {"country": "Italy", "name": "Bari"},
    {"country": "Italy", "name": "Catania"},
    {"country": "Italy", "name": "Venezia"},
    {"country": "Italy", "name": "Verona"},
    {"country": "Italy", "name": "Messina"},
    {"country": "Italy", "name": "Padova"},
    {"country": "Italy", "name": "Trieste"},
    {"country": "Italy", "name": "Brescia"},
    {"country": "Italy", "name": "Taranto"},
    {"country": "Italy", "name": "Parma"},
    {"country": "Italy", "name": "Prato"},
    {"country": "Italy", "name": "Modena"}
]

planets = [
    {"name": "Tatooine", "population": 200000, "area": 10465, "suns": 1, "moons": 3},
    {"name": "Coruscant", "population": 1000000000000, "area": 12240, "suns": 1, "moons": 4},
    {"name": "Naboo", "population": 4500000000, "area": 12120, "suns": 1, "moons": 3},
    {"name": "Endor", "population": 30000000, "area": 4900, "suns": 1, "moons": 9},
    {"name": "Hoth", "population": 1500, "area": 71500, "suns": 1, "moons": 3},
    {"name": "Kashyyyk", "population": 4500000000, "area": 444300, "suns": 1, "moons": 0},
    {"name": "Mustafar", "population": 20000, "area": 4209, "suns": 1, "moons": 0},
    {"name": "Yavin 4", "population": 1000, "area": 10224, "suns": 1, "moons": 1},
    {"name": "Jakku", "population": 2000000, "area": 16605, "suns": 1, "moons": 0},
    {"name": "Geonosis", "population": 100000000000, "area": 113700, "suns": 1, "moons": 0},
    {"name": "Alderaan", "population": 2000000000, "area": 12500, "suns": 1, "moons": 1},
    {"name": "Kamino", "population": 1000000000, "area": 19780, "suns": 1, "moons": 0},
    {"name": "Dagobah", "population": 1, "area": 22600, "suns": 1, "moons": 0},
    {"name": "Bespin", "population": 6000000, "area": 118000, "suns": 1, "moons": 0},
    {"name": "Utapau", "population": 95000000, "area": 12900, "suns": 1, "moons": 0},
    {"name": "Kessel", "population": 500000, "area": 310000, "suns": 1, "moons": 0},
    {"name": "Lothal", "population": 4500000000, "area": 143, "suns": 1, "moons": 2},
    {"name": "Mandalore", "population": 12000000000, "area": 988, "suns": 1, "moons": 3},
    {"name": "Sullust", "population": 1850000000, "area": 12780, "suns": 2, "moons": 0},
    {"name": "Takodana", "population": 500, "area": 10000, "suns": 1, "moons": 1},
    {"name": "Scarif", "population": 100000, "area": 500000, "suns": 1, "moons": 0},
    {"name": "Exegol", "population": 1000000, "area": 10000000, "suns": 1, "moons": 0},
    {"name": "Crait", "population": 10000, "area": 300000, "suns": 1, "moons": 0},
    {"name": "Ahch-To", "population": 1000, "area": 50000, "suns": 1, "moons": 0},
    {"name": "Jedha", "population": 1000000, "area": 200000, "suns": 1, "moons": 0},
    {"name": "Vulpter", "population": 10000000, "area": 400000, "suns": 1, "moons": 0},
    {"name": "Cantonica", "population": 2000000, "area": 600000, "suns": 1, "moons": 0},
    {"name": "Eadu", "population": 500000, "area": 150000, "suns": 1, "moons": 0},
    {"name": "Illum", "population": 10000, "area": 250000, "suns": 1, "moons": 0},
    {"name": "Nal Hutta", "population": 700000000, "area": 121500, "suns": 1, "moons": 5},
    {"name": "Stewjon", "population": 10000000, "area": 80000, "suns": 1, "moons": 2},
    {"name": "Haruun Kal", "population": 8000000, "area": 500000, "suns": 2, "moons": 0},
    {"name": "Socorro", "population": 3000000, "area": 80000, "suns": 1, "moons": 1},
    {"name": "Ryloth", "population": 1400000000, "area": 30600, "suns": 1, "moons": 5},
    {"name": "Dathomir", "population": 5200, "area": 125000, "suns": 2, "moons": 1},
    {"name": "Kalee", "population": 11000000, "area": 60000, "suns": 1, "moons": 3}
]

starships = [
    {"name": "Millennium Falcon", "model": "YT-1300 light freighter", "crew_capacity": 4, "length": 34.75, "width": 25.61},
    {"name": "X-wing Starfighter", "model": "T-65B X-wing starfighter", "crew_capacity": 1, "length": 12.5, "width": 11.76},
    {"name": "TIE Fighter", "model": "TIE/ln space superiority starfighter", "crew_capacity": 1, "length": 6.3, "width": 6.3},
    {"name": "Slave I", "model": "Firespray-31-class patrol and attack craft", "crew_capacity": 1, "length": 21.5, "width": 19.5},
    {"name": "Imperial Star Destroyer", "model": "Imperial I-class Star Destroyer", "crew_capacity": 37000, "length": 1600, "width": 1200},
    {"name": "Death Star", "model": "DS-1 Orbital Battle Station", "crew_capacity": 342953, "length": 160.7, "width": 160.7},
    {"name": "Executor", "model": "Executor-class Star Dreadnought", "crew_capacity": 279144, "length": 19000, "width": 6596},
    {"name": "TIE Advanced x1", "model": "TIE Advanced x1", "crew_capacity": 1, "length": 9.2, "width": 8.2},
    {"name": "Y-wing Starfighter", "model": "BTL Y-wing starfighter", "crew_capacity": 2, "length": 23.4, "width": 16.24},
    {"name": "B-wing Starfighter", "model": "A/SF-01 B-wing starfighter", "crew_capacity": 1, "length": 16.9, "width": 17.3},
    {"name": "A-wing Starfighter", "model": "RZ-1 A-wing interceptor", "crew_capacity": 1, "length": 9.6, "width": 6.9},
    {"name": "Naboo Royal Starship", "model": "J-type 327 Nubian royal starship", "crew_capacity": 8, "length": 76, "width": 36.9}
]

characters = [
    {"name": "Luke Skywalker", "height": 172, "weight": 77, "planet": "Tatooine"},
    {"name": "Princess Leia Organa", "height": 150, "weight": 49, "planet": "Alderaan"},
    {"name": "Han Solo", "height": 180, "weight": 80, "planet": "Corellia", "commands": "Millennium Falcon"},
    {"name": "Darth Vader", "height": 202, "weight": 136, "planet": "Tatooine", "commands": "Executor"},
    {"name": "Obi-Wan Kenobi", "height": 182, "weight": 77, "planet": "Stewjon"},
    {"name": "Yoda", "height": 66, "weight": 17, "planet": "Dagobah"},
    {"name": "Emperor Palpatine", "height": 173, "weight": 75, "planet": "Naboo"},
    {"name": "Chewbacca", "height": 228, "weight": 112, "planet": "Kashyyyk"},
    {"name": "R2-D2", "height": 109, "weight": 181, "planet": "Naboo"},
    {"name": "C-3PO", "height": 167, "weight": 75, "planet": "Tatooine"},
    {"name": "Lando Calrissian", "height": 177, "weight": 79, "planet": "Socorro"},
    {"name": "Boba Fett", "height": 183, "weight": 78, "planet": "Kamino", "commands": "Slave I"},
    {"name": "Padmé Amidala", "height": 165, "weight": 45, "planet": "Naboo"},
    {"name": "Qui-Gon Jinn", "height": 193, "weight": 89, "planet": "Coruscant"},
    {"name": "Mace Windu", "height": 188, "weight": 84, "planet": "Haruun Kal"},
    {"name": "Count Dooku", "height": 193, "weight": 86, "planet": "Serenno"},
    {"name": "Anakin Skywalker", "height": 188, "weight": 84, "planet": "Tatooine"},
    {"name": "Rey", "height": 170, "weight": 63, "planet": "Jakku"},
    {"name": "Finn", "height": 175, "weight": 73, "planet": "Unknown"},
    {"name": "Poe Dameron", "height": 176, "weight": 76, "planet": "Yavin 4"},
    {"name": "Kylo Ren", "height": 189, "weight": 89, "planet": "Unknown"},
    {"name": "Jabba the Hutt", "height": 320, "weight": 1500, "planet": "Nal Hutta"},
    {"name": "Grand Moff Tarkin", "height": 180, "weight": 82, "planet": "Eriadu"},
    {"name": "Darth Maul", "height": 175, "weight": 80, "planet": "Dathomir"},
    {"name": "Ahsoka Tano", "height": 170, "weight": 61, "planet": "Shili"},
    {"name": "General Grievous", "height": 216, "weight": 159, "planet": "Kalee"},
    {"name": "Wedge Antilles", "height": 170, "weight": 77, "planet": "Corellia"},
    {"name": "Admiral Ackbar", "height": 180, "weight": 83, "planet": "Mon Cala"},
    {"name": "Hera Syndulla", "height": 168, "weight": 57, "planet": "Ryloth"},
    {"name": "Asajj Ventress", "height": 170, "weight": 58, "planet": "Dathomir"},
    {"name": "Greedo", "height": 175, "weight": 74, "planet": "Rodia"}
]


def insert_countries():
    print("Creating list of Countries")
    for country in countries:
        country_token=Country()
        country_token.name = country
        db.session.add(country_token)
        db.session.commit()
        print("Country {} added to DataBase".format(country))

def insert_worldwide_cities():
    print("Creating list of States around the World")
    for city in cities:
        city_token=City()
        country = Country.query.filter_by(name=city["country"]).first()
        city_token.country_id = country.id
        city_token.name= city["name"]
        db.session.add(city_token)
        db.session.commit()
        print("{} from {} added to DataBase".format(city["name"], city["country"]))

def insert_planets():
    print("Creating list of Planets")
    for planet_data in planets:
        planet_token = Planets()
        planet_token.name = planet_data["name"]
        planet_token.population = planet_data["population"]
        planet_token.area = planet_data["area"]
        planet_token.suns = planet_data["suns"]
        planet_token.moons = planet_data["moons"]
        db.session.add(planet_token)
        db.session.commit()
        print("Planet {} added to DataBase".format(planet_data["name"]))

def insert_starships():
    print("Creating list of Starships")
    for starship_data in starships:
        starship_token = Starships()
        starship_token.name = starship_data["name"]
        starship_token.model = starship_data["model"]
        starship_token.crew_capacity = starship_data["crew_capacity"]
        starship_token.length = starship_data["length"]
        starship_token.width = starship_data["width"]
        db.session.add(starship_token)
        db.session.commit()
        print("Starship {} added to DataBase".format(starship_data["name"]))

def insert_characters():
    print("Creating list of Characters")
    for character_data in characters:
        character_token = Characters()
        character_token.name = character_data["name"]
        character_token.height = character_data["height"]
        character_token.weight = character_data["weight"]
        
        # Buscar el planeta en la base de datos y asignar su ID al personaje
        planet = Planets.query.filter_by(name=character_data["planet"]).first()
        if planet:
            character_token.planet_id = planet.id
        else:
            print(f"Warning: Planet '{character_data['planet']}' not found in the database.")
        
        # Si el personaje tiene una nave asignada, buscarla en la base de datos y asignar su ID al personaje
        if "commands" in character_data:
            starship = Starships.query.filter_by(name=character_data["commands"]).first()
            if starship:
                character_token.commands_id = starship.id
            else:
                print(f"Warning: Starship '{character_data['commands']}' not found in the database.")
        
        db.session.add(character_token)
        db.session.commit()
        print("Character {} added to DataBase".format(character_data["name"]))

