num=[2,5,1,7]
for i in num:
    print(i)
val=iter(num)
print(val.__next__())
print(val.__next__())