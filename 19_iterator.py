# All python collections have their own inbuilt iterators

list1 = list(("apple", "banana", "cherry", "guava"))
list_iter = list1.__iter__()

print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))

tuple1 = tuple(("apple", "mango", "pineapple"))

tuple_iter = tuple1.__iter__()

print(next(tuple_iter))
print(next(tuple_iter))
print(next(tuple_iter))

# Creating iterator for user made data types


class Count:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        x = self.num
        self.num += 1
        if x <= 10:
            return x
        else:
            raise StopIteration


C1 = Count()
Count_iter = iter(C1)
print(next(Count_iter))
print(next(Count_iter))
print(next(Count_iter))
print(next(Count_iter))
print(next(Count_iter))
print(next(Count_iter))
print(next(Count_iter))
