# set is a python collection.
# set is unordered, un-indexed, unchangeable and do not contain duplicate values.

set1 = {"apple", "cherry", "mango", 1, 2.50, True}
print(set1)
print(len(set1))
print(type(set1))

# accessing values of set
# indexing cannot access the set elements.
# we can either iterate through the set or check whether a value is present or not inside the set.

for x in set1:
    print(x)
if "cherry" in set1:
    print("cherry is present in set1")
else:
    print("cherry is not present in set1")

# we can add elements to a set using add()/update() methods.

set1.add("blue")
list1 = ["red", "green", "mango", 1, 2.50, True]
set1.update(list1)
print(set1)

# removing elements from a set
# we can use remove()/discard()/pop()/clear()/del function to remove set elements.
# pop() function removes the last element. Since we don't what the last element it is not possible to know which element
# will be removed.
# remove() returns an error if element is not present.
# discard() does not return an error if element is not present.
# clear() empty the set.
# del deletes the set.

set1.remove("cherry")
set1.discard("apple")
set1.clear()
del set1

# looping through a set.

set2 = set(list1)

for x in set2:
    print(x)

# union()/update() methods

set3 = {1, 2, 3, 4, 5}
set4 = {1, 4, 6, 0, 9}

print(set3)
print(set4)

set5 = set3.union(set4)
print(set5)

# intersection()/intersection_update()

set6 = set3.intersection(set4)
print(set6)

# symmetric_difference()/symmetric_difference_update()

set7 = set3.symmetric_difference(set4)
print(set7)
