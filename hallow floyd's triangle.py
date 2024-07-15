n=int(input())
num=1
for i in range(n):
    for j in range(i+1):
        if j==0 or i==n-1 or i==j:
            print(num,end=" ")
            num+=1
        else:
            print(" ",end=" ")
            num+=1
    print()