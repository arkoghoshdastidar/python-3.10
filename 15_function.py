# simple function definition
#######################################################################################################################
# AllFunctionDefinitionHere
def print_name(fname, mname, lname):
    print(fname + " " + mname + " " + lname)


def sum_of_number(*num):
    ret_sum = 0
    for x in range(len(num)):
        ret_sum += num[x]
    return ret_sum


def print_names(**name):
    print(name["fname"]+name["mname"]+name["lname"])


def sum_of_numbers_using_recursion(num):
    if num == 0:
        return 0
    else:
        return num + sum_of_numbers_using_recursion(num - 1)
#######################################################################################################################


print_name("arko", "ghosh", "dastidar")
print(sum_of_number(2, 3, 4, 5, 9))
print_names(fname="arko", mname="ghosh", lname="dastidar")
print(sum_of_numbers_using_recursion(10))
