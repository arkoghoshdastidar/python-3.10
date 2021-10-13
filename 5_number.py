import random

# There are three numeric data-types in python namely int, float and complex.

# int refer to integers with unlimited length.

i1 = 343351321178
print(i1)
print(type(i1))

# float refers to floating point numbers.

f1 = -32.21
print(f1)
print(type(f1))

# we can write floating point numbers in scientific notation also.

f2 = 2e2
print(f2)
print(type(f2))

# complex refers to complex numbers and the imaginary part of the complex number is suffixed by 'j'

c1 = 2 + 4j
print(c1)
print(type(c1))

# type conversion between numeric data types

x = int(1.10)   # float to int
y = float(1)    # int to float
z = complex(x)  # int to complex

print(x)
print(y)
print(z)

# NOTE: We cannot convert complex to any other numeric data t-pe.
# Generating random number using the random() which is present in the random module

random_number = random.randrange(0, 11, 1)
print(random_number)
