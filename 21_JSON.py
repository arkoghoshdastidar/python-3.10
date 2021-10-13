import json             # json is used to convert python objects to string and vice-versa



dict1={
    "name": "arnold",
    "age": 45,
    "weight": "68 kg"
}

x = json.dumps(dict1, indent=2)         # json.dumps(arg) convert python objects to strings
print(dict1)
y = json.loads(x)                       # json.loads(args) converts strings back to python objects
for x,z in y.items():
    print(x, z)
