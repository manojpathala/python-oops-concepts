def topten():
    n=1
    while n<=10:
        yield n
        n+=1
val=topten()

#using generator iterator is used without iter() function
print(val.__next__())
print(val.__next__())
#for i in val:
    #print(i)

