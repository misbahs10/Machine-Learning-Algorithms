f = open("sample.txt", "r+")
f.write("abc")
print(f.read())
f.close()