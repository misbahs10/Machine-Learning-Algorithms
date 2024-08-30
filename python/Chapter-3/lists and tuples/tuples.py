#             "tuples" Immutables means change nahi hoti 

tup = (1, 2, 4, 5)
print(tup)
print(type(tup))

tuple = (3,)   # important hai one element ko comma sy spread kar na.
print(tuple)   # agar comma sy spread nahi karyn gyn tu "integer" value assign karyga.
print(type(tuple))

#                            "tuples slicing".

slicing = ("hello", 78, "world", 67)
print(slicing[ :2])  
print(slicing[1:3])
print(type(slicing))