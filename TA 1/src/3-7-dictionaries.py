# assign
this_dict = {
    "key": "value",
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964}
# or
this_dict = dict(brand="Ford", model="Mustang", year=1964)

# Accessing Items
# Get the value of the "model" key:
x = this_dict["model"]
# or
x = this_dict.get("model")  # output: Mustang

# Change Values
this_dict["year"] = 2018

# Loop Through a Dictionary
# Print all key names in the dictionary, one by one:
for x in this_dict:
    print(x)

# Print all values in the dictionary, one by one:
for x in this_dict:
    print(this_dict[x])

for x in this_dict.values():
    print(x)

# Loop through both keys and values, by using the items() function:
for x, y in this_dict.items():
    print(x, y)

# Check if "model" is present in the dictionary:
if "model" in this_dict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

# length
print(len(this_dict))

# Adding Items
# Adding an item to the dictionary is done by using a new index key and
this_dict["color"] = "red"
print(this_dict)

# Removing Items
# The del keyword removes the item with the specified key name:
del this_dict["model"]

# The pop() method removes the item with the specified key name:
try:
    this_dict.pop("model")
    print(this_dict)
except:
    print("Cant pop a non existing key")

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
this_dict.popitem()
print(this_dict)

# Make a copy of a dictionary with the copy() method:
my_dict = this_dict.copy()

# The clear() keyword empties the dictionary:
this_dict.clear()

# The del keyword can also delete the dictionary completely:
del this_dict

# Nested Dictionaries
# Dictionaries in one dic.

my_family = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

# or
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

my_family = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

# More methods here:https://www.w3schools.com/python/python_ref_dictionary.asp
