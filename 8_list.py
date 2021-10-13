# lists are python collection.
#   1. ordered
#   2. changeable
#   3. duplicate values allowed

list1 = ["apple", "banana", "orange", "lemon"]
list2 = [1, 3, 4, 5]
list3 = ["apple", 3.5, 2]
list4 = list(("list", "using", "constructor"))

i = 0
while i < len(list1):
    print(list1[i])
    i += 1

x = 0

for x in list2:
    print(x)

print(list3)
print(list4)

# List slicing is done similar to string slicing.
# list_name[ starting_index : ending_index (not included) ]

print(list2[2:4])
print(list2[:4])
print(list2[2:])
print(list2[:])
print(list2[-4:])

# check whether an item is present in the list or not
if "apple" in list1:
    print("apple is present in list1")
else:
    print("apple not present in list1")

# replacing single list items

tempList = list(("python", "is", "awesome"))
tempList[0] = "cplusplus"
print(tempList)

# replacing range of elements in list

tempList[0:3] = ["python", "is", "fantastic"]
print(tempList)

# inserting value inside list

tempList.insert(2, "not")
print(tempList)

# appending list

tempList2 = list(("mango", "cherry"))
tempList2.append("guava")
print(tempList2)

# extending list

tempList2.extend(list1)
print(tempList2)

# removing element from a list

tempList2.remove("apple")
print(tempList2)

# popping element from a list

tempList2.pop(0)
print(tempList2)

# using del keyword

del tempList2[0]
print(tempList2)

# clearing the list

tempList2.clear()
print(tempList2)

del tempList2

numList = [1, 2, 3, -8, 12, 32, 20]
SUM = 0
for i in range(len(numList)):
    SUM += numList[i]
print("SUM = " + str(SUM))

print("printing numList")

i = 0
while i < len(numList):
    print(numList[i])
    i += 1

# list comprehension provides short hand for creating a list from another list

list6 = [x for x in list1 if "a" in x]
print("list1" + str(list1))
print("list6" + str(list6))

# list sorting
list2.insert(0, 5)
list2.append(-1)
print(list2)
list2.sort()    # By default ascending order
print(list2)
list2.sort(reverse=True)    # sort list in descending order
print(list2)
list2.reverse()
print(list2)        # reverse a list

# copy a list into another list by using list() constructor

list7 = list(list1)
print(list7)

# list concatenation using + operator or extend() method

list8 = list1+list3
print(list8)
list8.extend(list4)
print(list8)
