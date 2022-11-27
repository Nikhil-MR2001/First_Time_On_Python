n=int(input("enter the row size"))
for i in range(n):
    for j in range(n):
        print(" * ",end="")
    print("\n")

print("pattern2")
for i in range(3):
    for j in range(i+1):
        print(" * ",end="")
    print("\n")

print("pattern3")                   #here rowsize i=o     j=3
for i in range(3):                               #i=1     j=2
    for j in range(i,3):                         #i=2     j=1
        print(" * ",end="")
    print("\n")



print("patern5")
n=int(input("enter the no of rows"))
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("#", end=" ")
    print("\n")

print("pattern6")
n=int(input("enter the no of rows"))
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print("\n")

print("pattern7")
n = int(input("enter the no of rows"))
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,n-1):
        print("*", end=" ")
    for j in range(i,n):
        print("*", end=" ")
    print("\n")




print("pattern8")
n=int(input("enter the no of rows"))
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print("\n")

for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,n-1):
        print("*", end=" ")
    for j in range(i,n):
        print("*", end=" ")
    print("\n")
