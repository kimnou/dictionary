## Write a Python program to multiply all the items in a dictionary.

dict={1:10,2:10,3:10,4:10}
p1=1
p2=1
my_dict={}
for i in dict:
    p1=p1*i
    p2=p2*dict[i]
my_dict[p1]=p2
print(my_dict)


# dict={1:10,2:20,3:30,4:40,5:50}
# product=1
# for i in dict:
#     product=product*i
# print(product)
