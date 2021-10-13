# tuples are another kind of collection in python.
# tuples are ordered, unchangeable and can contain duplicate values.

tuple1 = ("apple", "mango", "cherry")   # tuple with single data-type str
tuple2 = ("carrot",)    # a tuple with single element must contain a comma after the element
tuple3 = (1, 2, 4, -1)  # integer tuple
tuple4 = ("apple", 2, 2.5, True)    # tuple can contain multiple data-types
tuple5 = tuple(("mango", "apple", 2.54, True, False))   # creating tuple using constructor

print("Length of tuple1 = "+str(len(tuple1)))
print(tuple1)
print("Type of tuple1 = "+str(type(tuple1)))

# Accessing elements in a tuple is same as that of strings/lists

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(tuple1[:3])
print(tuple1[-3:])

# checking whether an element is present inside a tuple or not

if "apple" in tuple1:
    print("apple is present in tuple1")
else:
    print("apple is not present in tuple1")

# modifying a tuple.
# since a tuple is immutable we cannot add,remove or change the contents of a tuple but we can do it indirectly.
# first convert a tuple into a list -> do the required changes -> convert the list back to a tuple.
# we can add two tuples directly using the + operator
# we can delete a tuple using 'del' keyword

list1 = list(tuple1)
list1[0] = "Apple"
list1.append("Orange")
tuple1 = tuple(list1)
print(tuple1)

# unpacking a tuple.
# python provides us a way to assign the values of a tuple to respective variables.
# if the number of variables are less than the number of elements in the tuple then we must use an * sign before a
# variable which would receive the remaining variables from the tuple as a list.

(red, yellow, *rest) = tuple1
print(red)
print(yellow)
print(rest)

# looping through a tuple

for x in tuple1:
    print(x)

for i in range(len(tuple1)):
    print(tuple1[i])

i = 0
while i < len(tuple1):
    print(tuple1[i])
    i += 1
