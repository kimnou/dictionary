## Write a Python program to sum all the items in a dictionary.

# dict={1:10,2:20,3:30,4:40,5:50}
# sum=0
# for i in dict:
#     sum=sum+i
# print(sum)


dict={1:10,2:20,3:30,4:40,5:50}
s1=0
s2=0
my_dict={}
for i in dict:
    s1=s1+i
    s2=s2+dict[i]
my_dict[s1]=s2
print(my_dict)
