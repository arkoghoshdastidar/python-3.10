# dictionaries in python are associative arrays.
# they are key-values pairs.

dict1 = {
    "name": "panda",
    "age": 21,
    "weight": 68
}

print(dict1)
print(len(dict1))
print(type(dict1))
print(dict1["name"])

# accessing elements.
# using 'get()' to access elements.

print(dict1.get("name"))
print(dict1.get("age"))
print(dict1.get("weight"))

# keys() method returns the list of keys of the dictionary.

DictKeys = dict1.keys()
print(DictKeys)

# values() method returns the list of values of the dictionary.

DictValues = dict1.values()
print(DictValues)

dict1["color"] = "red"

print(dict1.keys())
print(dict1.values())

# item() method will return the key-value pairs as a tuple in a list.

print(dict1.items())

# checking whether a key exists.

if "name" in dict1:
    print("name is " + dict1.get("name"))
else:
    print("no name key in dict1")

# adding/updating a dictionary

# adding a new value.
dict1["height"] = 178   # "height" : 178 added to dict1, this method can be used to update previous value.
print(dict1.keys())
print(dict1.values())
print(dict1.items())

# updating previous value

dict1.update({"weight": 69})    # update method can be used to add/update value in a dictionary.
print(dict1.items())

# removing dictionary items.
dict2 = dict(dict1)

dict1.pop("name")
print(dict1)

del dict1["age"]
print(dict1)

dict1.clear()
print(dict1)

del dict1

# looping through dictionary

for x in dict2:
    print(x)
for x in dict2:
    print(dict2.get(x))
for x in dict2.keys():
    print(x)
for x in dict2.values():
    print(x)
for x, y in dict2.items():
    print("{0} : {1}".format(x, y))

# copying a dictionary.

dict4 = dict(dict2)  # using dict() constructor to copy a dictionary.
print(dict4)

# nested dictionaries

children = {
    "child1": {
        "name": "rose",
        "age": 4
    },
    "child2": {
        "name": "velvet",
        "age": 10
    },
    "child3": {
        "name": "dante",
        "age": 3
    }
}
