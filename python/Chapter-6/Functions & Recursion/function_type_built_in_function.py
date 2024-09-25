# There are two types of functions.

# 1. Built-In Functions.
# built-in functions are the functions which are already defined in python and we can use them directly in our program. some examples of built-in functions are print(), len(), max(), min(), type(), range() etc

print("Fight-for-my-way","All-of-us-are-death",sep=" and ") # sep = ""
print("Extraordinary-you", end=" ")
print("Descendent-of-the-sun") # end = "\n"

# 2. user-defined Function.
# user-defined functions are the functions which are defined by the user. we can define our own functions we can define a function using def keyword.
# syntax of defining a function is: def function_name(parameters): return value and print. 

def calc_multi(a=2 , b=3):
    return a * b

print(calc_multi())

def calc_prod(a=4 , b=6):
    print(a * b)
    return a * b

calc_prod()