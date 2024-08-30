marks = int(input("Enter student marks : "))

if(marks >= 90):
    Grade = "A+"

elif(marks >= 80 and marks < 90):
    Grade = "A"
    
elif(marks >= 70 and marks < 80):
    Grade = "B"

else:
    Grade = "C"

print("Grade of the student ->", Grade)