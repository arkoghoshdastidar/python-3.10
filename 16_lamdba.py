# lambda functions are like inline functions
# func_name = lambda arguments : expression

x = lambda a: a+1

print(x(1))
print(x(2))
print(x(3))
print(x(4))

mul = lambda a, b: a*b

print(mul(2, 4))
print(mul(-2, 4))
print(mul(-2, -4))
print(mul(20, 0.4))


def multiplier(n):
    return lambda a: a*n


doubler = multiplier(2)
tripler = multiplier(3)

print(doubler(0))
print(doubler(1))
print(doubler(2))
print(doubler(3))
print(doubler(4))

print(tripler(0))
print(tripler(1))
print(tripler(2))
print(tripler(3))
print(tripler(4))
