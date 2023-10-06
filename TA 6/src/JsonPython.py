import json

from Hero import Hero

"""Create a json file from dictionary"""

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }}

# Let's turn it into a json file

with open("data.json", "w") as write_file:
    json.dump(data, write_file)

# As we can see, it's really hard to read, let's make it easier to read

with open("readable_data.json", "w") as write_file:
    json.dump(data, write_file, indent=4)

"""Create a dictionary from a json file"""

# Create data to read
h1 = Hero("Batman", 100)
h2 = Hero("Superman", 200)
h3 = Hero("GreenLantern", 150)
h4 = Hero("WonderWoman", 180)
h5 = Hero("Batgirl", 120)
h6 = Hero("Batkid", 90)
li = [h1, h2, h3, h4, h5, h6]
data2 = list()
for hero in li:
    data2.append({'name': hero.name, 'power': hero.power})

with open("heroes.json", "w") as fp:
    json.dump(data2, fp, indent=4)

with open("heroes.json", "r") as fp:
    data3 = json.load(fp)
# print(data3)
heroes = list()
for d in data3:
    #Recreating Hero objects from json
    name = d['name']
    power = d['power']
    heroes.append(Hero(name, power))
print(heroes)
