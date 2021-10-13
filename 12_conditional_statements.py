# if else ladder

a = 10
b = 20

if a < b:
    print("a < b")
elif a == b:
    print("a == b")
else:
    print("a > b")

# short hand if else ladder

print("a < b") if a < b else print("a = b") if a == b else print("a > b")

# and/or keywords in python

x = 1
y = 0
z = 2

print("x") if(x > y and x > z) else print("y") if(y > x and y > z) else print("z")

# nested if statements

a2 = 11

if a2 > 10:
    print("a2 > 10")
    if a2 < 20:
        print("10 < a2 < 20")
    else:
        print("a2 > 20")
else:
    print("a2 < 10")
