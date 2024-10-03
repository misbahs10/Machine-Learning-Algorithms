#                        Let's Practice

# Create a new file "practice.txt" using python. Add the following data in it:
# Hi everyone
# we are learning File I/0
# using Java.
# I like programming in Java.

with open("practice.txt", "w") as f:
    f.write("Hi everyone\nWe are learning File I/O\n")
    f.write("using Java\nI like programming in Java")

# WAF that replace all occurrences of "java" with "python" in above file.

with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)

print("------------")

# Search if the word "learning" exists in the file or not.

def check_for_word():

    with open("practice.txt", "r") as f:
        word = "learning"
        data = f.read()

        if(data.find(word)):
            print("Found")

        else:
            print("not found")

check_for_word()

# WAF to find in which line of the file does the word "learning" occur first.
# Print -1 if word not found.
def find_line():
    word = "12learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if (word in data):
            print(data.index(word))
            print("word found")
        else:
            print("not found")

find_line()
print("---------")

def check_word():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1

check_word()       

# From a file containing numbers separated by comma, print the
# # 49:03

count = 0
with open ("practice1.docx", "r") as f:
    data1 = f.read()
    print(data1)

    nums = data1.split(",")
    print(nums)

    nums = data1.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)

num = ""
for i in range(len(data1)):
    if(data1[i] == ","):
        print(int(num))
        num = ""
    else:
        num += data1[i]
        print(num)
