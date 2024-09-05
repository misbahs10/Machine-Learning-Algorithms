#                Let's Practice

# 1. Store following word meanings in a python dictionary :
#        table: "a piece of furniture", "list of facts & figures"
#        cat: "a small animal"

# dict = {
#     "table": ["a piece of furniture", "list of facts & figures"],
#     "cat": ["a small animal"]
# }

# print(dict)

# 2. You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
#        "python", "java", "C++", "python", "javascript",
#        "java", "python", "java", "C++", "C"

# sub = {
#     "python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"
# }

# print(sub)
# print(len(sub))

# 3. WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.

# marks = {}

# x = int(input("enter your PHY marks: "))
# marks.update({"PHY" : x})

# y = int(input("enter your MATH marks: "))
# marks.update({"MATH" : y})

# z = int(input("enter your CHEM marks: "))
# marks.update({"CHEM" : z})

# print(marks)

# Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)

set = {
    ("int", 9.0),
    ("float", 9)
}

print(type(set))
print(set)