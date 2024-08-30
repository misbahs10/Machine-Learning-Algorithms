#                              Let Practice.

# 1.  Write a program to input user's first name and print its length.

name = input("what's your name: ")
print("length of your name is: ",len(name))

# 2.  Write a program to find the occurrence of '$' in a string.

dollar ="Hi, i am a $ symbol and $ 566.44 $"
print(dollar.count('$'))

# 3.  Write a program to check if a number entered by the user is odd or even.

num = int(input("Enter number: "))


if (num % 2 == 0):
    print("Number is even")

else:
    print("Number is odd")

# 4. Write a program to find the greatest of 4 numbers entered by the user.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter forth number: "))

if (a >= b and a >= c and a >= d):
    print("first number is largest", a)

elif (b >= c and b >= d):
    print("second number is largest", b)

elif (c >= d):
    print("third number is largest", c)

else:
    print("forth number is largest", d)

# 5. Write a program to check if a numbers is a multiple of 7 or not.

num = int(input("Enter number: "))

if (num % 7 == 0):
    print("Number is multiple of 7")

else:
    print("Number is not multiple of 7")
