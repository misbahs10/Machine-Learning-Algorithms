a = 3
b = 6

def sum (a, b):
    return a + b

print(sum(a, b))

print("------")

def calc_sum (x, y):
    sum = x + y
    print(sum)
    return sum

calc_sum(3, 12)

print("------")

calc_sum(3, 10)

print("more lines of code")

calc_sum(45, 3)

# function definition
def calc_add (a, b): #----> parameters
    return a + b

sum = calc_add(2, 4) # calc_sum ----> function call and (2, 4) ----> arguments
print(sum)

def greeting():
    print("hello")

greeting()

# we want to create a function which calculate the average of 3 numbers

def calc_avg(a, b, c):
    return (a + b + c) / 3

avg = calc_avg(2, 5, 7)
print(avg)

print("------")

def calc_thr(a, b, c):
    sum = a + b + c
    thr = sum / 3
    return thr

print(calc_thr(2, 5, 7))  # Output: 4.666