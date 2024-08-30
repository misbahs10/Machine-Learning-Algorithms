#  "Append" method means element ko last main joint karta hai.
print("Append......")

list = ["Goblin", 45, "All of us are death"]
print("Before:", list)

list.append("are mortal")
print("After:", list)  

#  "Insert" method means element ko specific position par add karta hai.

print("Insert......")

list = ["Mr queen", 564, 67, ]
print("Before:", list)

list.insert(5, "I am a queen")
print("After:", list) 

#  "Sort" method means list ko ascending order main karta hai.

print("Sort......")

list = [34, 75, 2, 90]
print("Before:", list)

list.sort()
print("After:", list) 

# "Sort(reverse = True)" method list ko descending order main karta hai.

print("Sort (reverse = True)......")

list = [56, 3, 8, 9]
print("Before:", list)

list.sort(reverse = True)
print("After:", list)

#  "Reverse" method means list ko reverse karta hai.

print("Reverse......")

list = [3, 6, 1, 8]
print("Before:", list)

list.reverse()
print("After:", list)  

#  "Remove" method means removes first occurrence of element.

print("Remove......")

list = ["Mr queen", "I am a queen", "are mortal"]
print("Before:", list)

list.remove("I am a queen")
print("After:", list)

# "Pop" method means removes element at index

print("Pop......")

list = [43, 8, 0 ,1]
print("Before:", list)

list.pop(2)  #  index (2)
print("After:", list)