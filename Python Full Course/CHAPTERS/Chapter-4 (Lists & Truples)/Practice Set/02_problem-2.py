# Write a program to accepect marks of 6 students andd display them in a sorted manner.


marks = []

# This problem in Integer
s1 = int(input("Enter the mark here: "))
marks.append(s1)
s2 = int(input("Enter the mark here: "))
marks.append(s2)
s3 = int(input("Enter the mark here: "))
marks.append(s3)
s4 = int(input("Enter the mark here: "))
marks.append(s4)
s5 = int(input("Enter the mark here: "))
marks.append(s5)
s6 = int(input("Enter the mark here: "))
marks.append(s6)

marks.sort() # Make it short number sytsem

print(marks)