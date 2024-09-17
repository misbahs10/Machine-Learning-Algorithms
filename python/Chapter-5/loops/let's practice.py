# #                   LET'S PRACTICE

# # 1. print number from 1 to 100

i = 1
while i <= 100:
    print(i)
    i += 1

# # 2. print number from 100 to 1

i = 100
while i >= 1:
    print(i)
    i -= 1

# # 3. print the multiplication table of a number n

n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(n * i)
    i += 1

# # 4. print the elements of the following list using a loop:
# # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
heroes = ["ironman", "spiderman", "thor"]

idx = 0
while idx < len(heroes):
    print(heroes[idx])
    idx += 1

# # Search for a number x in this tuple using loop:
# # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

idx = 0
while idx < len(tuple):
    print(tuple[idx])
    idx += 1

nums1 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 25
idx = 0
while idx < len(nums1):
    if nums1[idx] == x:
        print("found at idx", idx)
    else:
        print("finding...")
    idx += 1

# Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

chr = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for idx in chr:
    print(idx)

# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

x = int(input("enter: "))
x = int(x)

int = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

for idx in int:
    if idx == x:
        print("found at idx", idx)

# WAP to find the sum of first n numbers. (using while)

n = 10
sum = 0

for el in range(1, n+1):
    sum += el

print("total sum =", sum)

m = 7
add = 0
i = 1

while i <= m:
    add += i
    i += 1

print("total sum =", sum)

# WAP to find the factorial of first n numbers. (using for)

n = 3
fact = 1
i = 1

for i in range(1, n+1):
    fact *= i
    print("factorial of", n, "is", fact)

m = 5
fact = 1
i = 1

while i <= n:
    fact *= 1
    i += 1

print("factorial =", fact)