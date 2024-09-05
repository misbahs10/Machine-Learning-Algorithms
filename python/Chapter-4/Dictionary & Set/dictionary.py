dict = {
    "name" : "Misbah",
    "age" : 18.5,
    "marks" : [66.87, 60.76, 100],
}

dict["age"] = 20
dict["marks"] = 75.78
dict["is-adult"] = True

print(dict)

print("------------------") # nested dictionary.

student = {
    "name" : "Misbah",
    "subjects" : {
        "math" : 100,
        "science" : 87,
        "english" : 76
    }
}

print(student)
print(student["subjects"])
print(student["subjects"]["math"])  # Output: 100