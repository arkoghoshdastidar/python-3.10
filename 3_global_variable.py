#   variables that are declared outside a function is called global variables.
#   global variables can be used both inside and outside functions.

var = "awesome"


def my_func():
    print("python is " + var)


my_func()

#   variable declared inside a function is local to the function and can be used only inside the function.


def my_func_2():
    var = "fantastic"
    print("python is " + var)


my_func_2()
print("python is " + var)

#   we can use the 'global' keyword to create a global variable inside a function/change the value of the global varible
#   inside a function.


def my_func_3():
    global var
    var = "fantastic"


print("python is " + var)
my_func_3()
print("python is " + var)
