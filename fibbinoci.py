def fs(n):
    x,y,z=-1,1,0
    for i in range(0,n):
        z=x+y
        x=y
        y=z
    print(z,end=" ")
n=int(input("Enter the number:"))
fs(n)