## Write a Python program to convert a list into a nested dictionary of keys.
## num_list = [1, 2, 3, 4]
## Sample output: {1: {2: {3: {4: {}}}}}


# list=[1,2,3,4]
# value={}
# dict={}
# for i in list:
#     dict[i]=value
# print(dict)

list=[1,2,3,4]
a={}
b={}
new=a=b={}
for i in list:
    b[i]={}
    b=b[i]
print(new)