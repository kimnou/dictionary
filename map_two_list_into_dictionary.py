## Write a Python program to map two lists into a dictionary.

list1=["a","b","c","d","e","f","g"]
list2=[1,2,3,4,5,6,7]
l=len(list1)
dict={}
for i in range(l):
    dict[list1[i]]=list2[i]
print(dict)
