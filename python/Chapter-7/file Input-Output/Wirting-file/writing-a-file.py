f = open("inbox.txt", "w")
f.write("Hello, world!")
f.close()

f = open("inbox.txt", "a")
f.write("\tI want to learn JS tomorrow.")
f.write("\nThen I'll move to TypeScript.")
f.close()
