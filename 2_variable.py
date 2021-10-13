#   variables are created at the time of declaration in python.

x = 5
y = "Hello, World"

print(x)
print(y)

#   variables can even change type after the have been initialized in python

z = 5
z = "python"

print(z)

#   inorder to create a variable of a particular type we can use type-casting

a = int(3)  # a = 3 integer variable
print(type(a))
a2 = str(3)  # a2 = '3' character variable
print(type(a2))
a3 = float(3)  # a3 = 3.0 floating point variable
print(type(a3))

#   variable names are case sensitive

myVar = "python"
MyVar = "python programming"

print(myVar)
print(MyVar)

#   python allows us to assign multiple values to multiple variables in a single line
var1, var2, var3 = "red", "yellow", "blue"
print(var1)
print(var2)
print(var3)

#   single values to multiple variables
var4 = var5 = var6 = "voilet"

print(var4)
print(var5)
print(var6)

# + operator is used to concatenate strings in python

strVar1 = "python"
strVar2 = " is awesome"
print(strVar1 + strVar2)
