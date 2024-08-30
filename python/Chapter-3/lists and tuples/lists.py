marks = [65.4, 73.7, 98.5, 67.6]

print(marks)
print(len(marks))
print(marks[0])
print(marks[1])
print(type(marks))

# string ---> immutable means jo change nahi ho sakti.
# list ---> mutable means jo change ho jay.
# (tuple is like string but we can store multiple values in it).

drama = ["The Heirs", "Secret Garden", "Reply 1988"]
print(drama)

drama[2] = "Hotel Del Luna"
print(drama)  # Reply 1988 is replaced by Hotel Del Luna
# drama[3] = "Crash Landing on You"  # This will give an error