# stuff same as lists:
# Access Tuple Items
# Negative Indexing
# Range of Indexes
# Loop Through a Tuple
# Check if Item Exists
# Tuple Length
# create tuple with one item:
# One item tuple, remember the commma:
this_tuple = ("apple",)
print(type(this_tuple))
# NOT a tuple
this_tuple = ("apple")
print(type(this_tuple))

# Change Tuple Values
# you can't!, but convert to list then convert back to tuple:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

# tuple method:
this_tuple = tuple(("apple", "banana", "cherry"))
# Return the number of times the value 5 appears in the tuple:
this_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(this_tuple.count(5))

# Search for the first occurrence of the value 8, and return its position:
this_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(this_tuple.index(8))
# https://www.w3schools.com/python/python_ref_tuple.asp
