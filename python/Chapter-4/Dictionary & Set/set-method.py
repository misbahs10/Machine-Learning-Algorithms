#                    SET METHOD IN PYTHON.

# (.add(ele))  adds an element to the set

collection = {"Moana", 23, " Toy Story ", 5.6}

collection.add("The Lion King")
collection.add(1)
print(collection)

# (.remove(ele)) removes an element from the set

collection = {"Moana", 23, " Toy Story ", 5.6, "the king land"}

collection.remove("the king land")
print(collection)

# (.pop()) removes a random value

collection = {"Moana", 23, " Toy Story ", 5.6}

collection.pop()
print(collection)

# (.clear()) empties the set

collection = {"Moana", 23, " Toy Story ", 5.6, "the king land"}

collection.clear()
print(collection)

# (.union(set2)) combines both set values and returns new

set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}

print(set1.union(set2))
print(set1)
print(set2)

# (.intersection(set2)) combines common values and returns new

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

print(set1.intersection(set2))
print(set1)
print(set2)