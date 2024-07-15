n=int(input("Enter the number:"))
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i+1):
        if j==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(i):
        if i==j+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for k in range(n+1):
    for l in range(k):
        print(" ",end=" ")
    for l in range(n-k):
        if l==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for l in range(n+1-k):
        if k+l==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

