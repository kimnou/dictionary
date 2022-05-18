user=int(input("enter length of dict:"))
i=0
mydict={}
while i<user:
    k=input("enter key:")
    v=input("enter value:")
    mydict[k]=v
    i+=1
print(mydict)

