"Assignment 1"

import random


l=[]
n=int(input("Enter the number of students whoose details are supposed to be entered:"))

for i in range(n):
    a=str(input("Enter student name:"))
    b=random.randint(1,10)        
    c=float(input("Enter student percentage:"))
    d=[b,a,c]
    l.append(d)
k=len(l)
for j in range (k):
    print(l[j])


    

