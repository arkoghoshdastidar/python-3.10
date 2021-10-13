import MyModule as myModule

print(dir(myModule))
myModule.greetings("Aron")
myModule.print_full_name("Aron", "Blaze")

# Importing only a part of the module
from MyModule import greetings

# Taking input from user

name = input("Enter UserName : ")
myModule.greetings(name)
greetings(name)
