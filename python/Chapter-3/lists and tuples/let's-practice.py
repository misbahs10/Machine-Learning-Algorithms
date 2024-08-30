# write a program to ask the user to enter names of 3 favorite movies and store them in a list.

movies = []

mov1 = input("Enter first movie: ")
movies.append(mov1)
mov2 = input("Enter second movie: ")
movies.append(mov2)
mov3 = input("Enter third movie: ")
movies.append(mov3)

print(movies)

# write a program to check if a list contains a palindrome of elements. (Hint: use copy() method)   # [1, 2, 3, 2, 1]         [1, "abc", "abc", 1]

lst1 = [1, 2, 3, 2, 1]

copy_lst1 = lst1.copy()
copy_lst1.reverse()

if (copy_lst1 == lst1):
    print("List contains a palindrome of elements")

else:
    print("List does not contain a palindrome of elements")

# write a program to count the number of students with the "A" grade in the following tuple. ["C", "D", "A", "A", "B", "B", "A"]
# store the above values in a list and sort them from "A" to "D".

Grade = ("C", "D", "A", "A", "B", "B", "A")
print(Grade)
print(Grade.count("A"))

grades = ["C", "D", "A", "A", "B", "B", "A"]
grades.sort()
print(grades)
