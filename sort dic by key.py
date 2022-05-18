### Write a Python program to sort a dictionary by key.

# dict={4:"a",1:"b",3:"c",2:"d"}
# p=sorted(dict.keys())
# mydict={}
# for i in p:
#     mydict[i]=dict[i]
# print(mydict)


mydict={'c':4,'a':2,'b':1,'d':3}
s=sorted(mydict.keys())
dict={}
for i in s:
    dict[i]=mydict[i]
print(dict)

