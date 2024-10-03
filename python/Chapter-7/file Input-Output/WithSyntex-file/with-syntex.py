with open("sample.docx", "r") as f:
    data = f.read()
    print(data)

with open("sample.docx", "w") as f:
    f.write("new data")