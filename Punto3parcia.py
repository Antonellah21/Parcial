jedis = [
    {"name": "Qui-Gon Jinn", "rank": "Jedi Master", "species": "Human", "master": "Tera Sinube/Count Dooku", "lightsaber_color": "Green", "homeworld": "Coruscant", "birth_year": "79ABY", "height": 1.93, "to_darkside": None, "come_lightside": None},
    {"name": "Obi-Wan Kenobi", "rank": "Jedi Master", "species": "Human", "master": "Qui-Gon Jinn/Yoda", "lightsaber_color": "Blue", "homeworld": "Stewjon", "birth_year": "57ABY", "height": 1.82, "to_darkside": None, "come_lightside": None},
    {"name": "Anakin Skywalker/Darth Vader", "rank": "Jedi Knight", "species": "Human", "master": "Obi-Wan Kenobi", "lightsaber_color": "Blue", "homeworld": "Tatooine", "birth_year": "41ABY", "height": 1.88, "to_darkside": True, "come_lightside": True},
    {"name": "Quinlan Vos", "rank": "Jedi Master", "species": "Human/Kiffar", "master": "Tholme", "lightsaber_color": "Green", "homeworld": "Kiffu", "birth_year": "59ABY", "height": 1.91, "to_darkside": True, "come_lightside": False},
    {"name": "Yoda", "rank": "Grand Master", "species": None, "master": None, "lightsaber_color": "Green", "homeworld": None, "birth_year": "896ABY", "height": 0.66, "to_darkside": None, "come_lightside": None},
    {"name": "Mace Windu", "rank": "Jedi Master/Master of the Order", "species": "Human", "master": "Cyslin Myr", "lightsaber_color": "Purple", "homeworld": "Haruun Kal", "birth_year": "72ABY", "height": 1.92, "to_darkside": None, "come_lightside": None},
    {"name": "Ki-Adi-Mundi", "rank": "Jedi Master", "species": "Cerean", "master": None, "lightsaber_color": "Purple/Blue", "homeworld": "Cerea", "birth_year": "92ABY", "height": 1.98, "to_darkside": None, "come_lightside": None},
    {"name": "Plo Koon", "rank": "Jedi Master", "species": "Kel Dor", "master": None, "lightsaber_color": "Yellow/Blue/Orange", "homeworld": "Dorin", "birth_year": "71ABY", "height": 1.88, "to_darkside": None, "come_lightside": None},
    {"name": "Saesee Tiin", "rank": "Jedi Master", "species": "Iktotchi", "master": None, "lightsaber_color": "Green", "homeworld": "Iktotch", "birth_year": None, "height": 1.93, "to_darkside": None, "come_lightside": None},
    {"name": "Yaddle", "rank": "Jedi Master", "species": None, "master": None, "lightsaber_color": "Green", "homeworld": None, "birth_year": "509AYB", "height": 0.61, "to_darkside": None, "come_lightside": None},
    {"name": "Even Piell", "rank": "Jedi Master", "species": "Lannik", "master": None, "lightsaber_color": "Green", "homeworld": "Lannik", "birth_year": None, "height": 1.22, "to_darkside": None, "come_lightside": None},
    {"name": "Oppo Rancisis", "rank": "Jedi Master", "species": "Thisspiasian", "master": "Yaddle", "lightsaber_color": "Green", "homeworld": "Thisspias", "birth_year": "206ABY", "height": 1.38, "to_darkside": None, "come_lightside": None},
    {"name": "Adi Gallia", "rank": "Jedi Master", "species": "Tholothian", "master": None, "lightsaber_color": "Green/Blue", "homeworld": "Coruscant", "birth_year": None, "height": 1.84, "to_darkside": None, "come_lightside": None},
    {"name": "Yarael Poof", "rank": "Jedi Master", "species": "Quermian", "master": None, "lightsaber_color": "Blue", "homeworld": "Quermia", "birth_year": None, "height": 2.64, "to_darkside": None, "come_lightside": None},
    {"name": "Eeth Koth", "rank": "Jedi Master", "species": "Zabrak", "master": None, "lightsaber_color": "Green/Blue", "homeworld": "Iridonia", "birth_year": None, "height": 1.71, "to_darkside": None, "come_lightside": None},
    {"name": "Depa Billaba", "rank": "Jedi Master", "species": "Chalactan", "master": None, "lightsaber_color": "Green", "homeworld": "Chalacta", "birth_year": None, "height": 1.68, "to_darkside": None, "come_lightside": None},
    {"name": "Kit Fisto", "rank": "Jedi Master", "species": "Nautolan", "master": None, "lightsaber_color": "Green", "homeworld": "Glee Anselm", "birth_year": None, "height": 1.96, "to_darkside": None, "come_lightside": None},
    {"name": "Luminara Unduli", "rank": "Jedi Master", "species": "Mirialan", "master": None, "lightsaber_color": "Green", "homeworld": "Mirial", "birth_year": "58ABY", "height": 1.76, "to_darkside": None, "come_lightside": None},
    {"name": "Barriss Offee", "rank": "Padawan", "species": "Mirialan", "master": "Luminara Unduli", "lightsaber_color": "Blue", "homeworld": "Mirial", "birth_year": "40ABY", "height": 1.66, "to_darkside": True, "come_lightside": False},
    {"name": "Shaak Ti", "rank": "Jedi Master", "species": "Togruta", "master": None, "lightsaber_color": "Blue", "homeworld": "Shili", "birth_year": None, "height": 1.87, "to_darkside": None, "come_lightside": None},
    {"name": "Coleman Trebor", "rank": "Jedi Master", "species": "Vurk", "master": None, "lightsaber_color": "Green", "homeworld": "Sembla", "birth_year": None, "height": 2.13, "to_darkside": None, "come_lightside": None},
    {"name": "Jocasta Nu", "rank": "Jedi Master", "species": "Human", "master": None, "lightsaber_color": "Blue", "homeworld": "Coruscant", "birth_year": None, "height": 1.69, "to_darkside": None, "come_lightside": None},
    {"name": "Aayla Secura", "rank": "Jedi Knight", "species": "Twi'lek", "master": "Quinlan Vos", "lightsaber_color": "Blue", "homeworld": "Ryloth", "birth_year": "47ABY", "height": 1.72, "to_darkside": None, "come_lightside": None},
    {"name": "Sifo-Dyas", "rank": "Jedi Master", "species": "Human", "master": None, "lightsaber_color": "Green", "homeworld": "Mundos Cassandranos", "birth_year": "75ABY", "height": None, "to_darkside": None, "come_lightside": None},
    {"name": "Count Dooku", "rank": "Jedi Master", "species": "Human", "master": "Yoda", "lightsaber_color": "Blue/Red", "homeworld": "Serenno", "birth_year": "102ABY", "height": 1.93, "to_darkside": True, "come_lightside": False},
    {"name": "Ahsoka Tano", "rank": "Padawan", "species": "Togruta", "master": "Anakin Skywalker", "lightsaber_color": "Green/Yellow/White", "homeworld": "Shili", "birth_year": "36ABY", "height": 1.88, "to_darkside": None, "come_lightside": None},
    {"name": "Rey Skywalker", "rank": "Padawan", "species": "Human", "master": "Leia Organa/Luke Skywalker", "lightsaber_color": "Blue", "homeworld": "Jakku", "birth_year": "15DBY", "height": 1.70, "to_darkside": None, "come_lightside": None},
    {"name": "Ben Solo", "rank": "Jedi Knight", "species": "Human", "master": "Luke Skywalker", "lightsaber_color": "Blue", "homeworld": "Chandrila", "birth_year": "5DBY", "height": 1.89, "to_darkside": True, "come_lightside": True}
]

def listar_jedis(jedis):
    return [jedi["name"] for jedi in jedis]

def info_jedi(jedis, nombre):
    for jedi in jedis:
        if jedi["name"] == nombre:
            return jedi
    return None
print("Lista de todos los Jedi:", listar_jedis(jedis))
print()
def find_jedi_by_name(name):
    for jedi in jedis:
        if jedi["name"] == name:
            return jedi
    return None

names_to_find = ["Ahsoka Tano", "Kit Fisto"]

for jedi in jedis:
    if jedi["name"] in names_to_find:
        print("###", jedi["name"])
        for key, value in jedi.items():
            print("- **{}**: {}".format(key.capitalize().replace("_", " "), value))
        print()
print()
def find_padawans(master_name):
    padawans = []
    for jedi in jedis:
        if jedi["master"] == master_name:
            padawans.append(jedi)
    return padawans

yoda_padawans = find_padawans("Yoda")
print("Padawans de Yoda:")
for padawan in yoda_padawans:
    print(padawan["name"])

luke_padawans = find_padawans("Luke Skywalker")
print("\nPadawans de Luke Skywalker:")
for padawan in luke_padawans:
    print(padawan["name"])
print()
def find_jedi_by_species(species_name):
    jedis_species = []
    for jedi in jedis:
        if jedi["species"] == species_name:
            jedis_species.append(jedi)
    return jedis_species

human_jedis = find_jedi_by_species("Human")
print("Jedis de especie humana:")
for jedi in human_jedis:
    print(jedi["name"])

twilek_jedis = find_jedi_by_species("Twi'lek")
print("\nJedis de especie Twi'lek:")
for jedi in twilek_jedis:
    print(jedi["name"])
print()

def find_jedi_by_name_starting_with_A():
    jedis_with_A = []
    for jedi in jedis:
        if jedi["name"].startswith("A"):
            jedis_with_A.append(jedi)
    return jedis_with_A

jedis_with_A = find_jedi_by_name_starting_with_A()
print("Jedis cuyos nombres comienzan con 'A':")
for jedi in jedis_with_A:
    print(jedi["name"])

print()
    
def find_jedi_with_multiple_lightsaber_colors():
    jedis_with_multiple_colors = []
    for jedi in jedis:
        colors = jedi["lightsaber_color"].split("/")
        if len(colors) > 1:
            jedis_with_multiple_colors.append(jedi)
    return jedis_with_multiple_colors

jedis_with_multiple_colors = find_jedi_with_multiple_lightsaber_colors()
print("Jedis que han usado sable de luz de más de un color:")
for jedi in jedis_with_multiple_colors:
    print(jedi["name"])  
print()
    
def find_jedi_with_yellow_or_violet_lightsaber():
    jedis_with_yellow_or_violet = []
    for jedi in jedis:
        if jedi["lightsaber_color"] == "Yellow" or jedi["lightsaber_color"] == "Purple" or jedi["lightsaber_color"] == "Violet":
            jedis_with_yellow_or_violet.append(jedi)
    return jedis_with_yellow_or_violet

jedis_with_yellow_or_violet = find_jedi_with_yellow_or_violet_lightsaber()
print("Jedis que han utilizado sable de luz amarillo o violeta:")
for jedi in jedis_with_yellow_or_violet:
    print(jedi["name"])

print()
    
def encontrar_padawans(maestro):
    padawans = []
    for jedi in jedis:
        if maestro in jedi.get("master", "").split('/'):
            padawans.append(jedi["name"])
    return padawans

def encontrar_padawans(maestro):
    padawans = []
    for jedi in jedis:
        if jedi["master"] is not None and maestro in jedi["master"]:
            padawans.append(jedi["name"])
    return padawans

padawans_quigon_jinn = encontrar_padawans("Qui-Gon Jinn")


padawans_mace_windu = encontrar_padawans("Mace Windu")

print("Padawans de Qui-Gon Jinn:", padawans_quigon_jinn)
print("Padawans de Mace Windu:", padawans_mace_windu)
print()
jedi_grand_master = []

for jedi in jedis:
    if jedi["rank"] == "Grand Master":
        jedi_grand_master.append(jedi)

print("Jedi Grand Master:")
for jedi in jedi_grand_master:
    print(jedi["name"])