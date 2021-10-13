# for loop can be used to traverse through indexed as well as un-indexed collections.

fruits = ["apple", "mango", "banana", "cherry"]

for x in fruits:
    if x == "cherry":
        continue
    print(x)
else:
    print("fruits list completely traverse!!")

# range function range(starting_index, last_index, step)

for x in range(1, 11, 2):
    print(x)
else:                              # NOTE: The else block will not be executed if the loop is broken by break statement
    print("for loop traversed successfully!!")

