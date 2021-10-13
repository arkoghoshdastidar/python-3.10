# Anything between a single or double quotes is considered as string.
print("Hello, World")

# Assigning string to a variable
x = "Hello, World"
print(x)

# Assigning multiline string to a variable
x = """ Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(x)
length = str(len(x))
print("length of " + x + " = " + length)
# string are array of characters.
# len() function returns the length of a string.
for i in "python":
    print(i)

# check whether a phrase or character is present in a string or not, we use 'in' keyword

if "lorem" in x:
    print("lorem present in x")
else:
    print("lorem not present in x")

# check whether a phrase or character is present using 'not in' keyword

if "ipsum" not in x:
    print("ipsum is not present in x")
else:
    print("ipsum is present in x")

