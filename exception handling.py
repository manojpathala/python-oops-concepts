a=int(input("enter value of a:"))
b=int(input("enter value of b:"))

try:
    print("resource open")
    print(a/b)
    k=int(input("enter value of k:"))
    i=int(input("enter valuo of i:"))
    print(k*i)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print("some thing went wrong:",e)
finally:
    print("resource closed")