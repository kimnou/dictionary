i=0
a=[]
b=[]
while i<10:
    name=input("enter name:")
    mark=int(input("enter marks:"))
    a.append(name)
    b.append(mark)
    dict={}
    for j in range (len(a)):
        dict[a[j]]=b[j]
    i+=1
print(dict)
