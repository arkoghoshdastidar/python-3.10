"""Slicing
You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, to return a part of the string."""

#    0                        25    : +ve index
x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#   -26                      -1     : -ve index
print(x[0:5])
print(x[2:5])
print(x[:])
print(x[-10:])

# upper() converts a string from lower case to upper case
str1 = "abcdef"
str1 = str1.upper()
print(str1)

# lower() method converts the string from upper case to lower case
str1 = str1.lower()
print(str1)

# len() returns the length of the string
print(len(str1))

# replace(from, to)
str1 = str1.replace("a", "   ")
print(str1)

# strip() method removes the white-spaces from the beginning and end of the string.
str1 = str1.strip()
print(str1)

# + operator can be used to concatenate two strings.
str1 = str1.upper() + str1.lower()
print(str1)

# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {}
# are:
# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

potatoes = 300
sugar = 0.5
str2 = "I want {0}g potatoes and {1}kg sugar."
str2 = str2.format(potatoes, sugar)
print(str2)
