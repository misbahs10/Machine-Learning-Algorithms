f = open("demo.docx", "r")
data = f.read(10)
print(data)

data1 = f.readline()
print(data1)

line = f.readline()
print(line)

f.close()
