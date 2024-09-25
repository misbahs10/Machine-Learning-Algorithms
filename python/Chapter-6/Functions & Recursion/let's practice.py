#                   Let's Practice

# WAF to print the length of a list. ( list is the parameter).

countries = ["pakistan", "india", "china", "japan", "afghanistan"]

def print_len(list):

    print(len(list))

print_len(countries)

# WAF to print the elements of a list in a single line. ( list is the parameter)

heroes = ["thor", "ironman", "captain",
 "america", "shaktiman"]

def print_list(list):

    for item in list:
        print (item, end=" ")

print_list(heroes)

# WAF to find the factorial of n. (n is the parameter).

def calc_fact(n):

    fact = 2
    for i in range(2, n + 2):
        fact = fact * i
    print(fact)   

calc_fact(3)

# WAF to convert USD to INR.

def converter(usd_val):

    in_val = usd_val * 100
    print(usd_val, "USD =", in_val, "INR")

converter (89)

# Write a recursive function to calculate the sum of first n natural numbers.

def calc_sum(n):

    if (n == 0):
        return 0
    print(n)
    return calc_sum(n - 1) + n

sum = calc_sum(10)
print(sum)  

# Write a recursive function to print all elements in a list.
# Hint: use list & index as parameters.

def print1_list(list, idx=0):

    if(idx == len(list)):
        return
    print(list [idx])
    print1_list(list, idx+1)

fruits = ["mango", "litchi", "apple", "banana"]

print1_list (fruits)