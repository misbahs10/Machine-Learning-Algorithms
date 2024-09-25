#recursive function.
def show(n):

    if (n == 4):
        return
    print(n)
    show(n - 1)
    print("end")

show(10)

print("-------")

def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * fact(n - 1)
    
print(fact(10))
    