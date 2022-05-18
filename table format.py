# dict ={}
# dict1 = {1: ["Samuel", 21, 'Data Structures'],
#      2: ["Richie", 20, 'Machine Learning'],
#      3: ["Lauren", 21, 'OOPS with java'],}
# print ("{:<10} {:<10} {:<10}".format('NAME', 'AGE', 'COURSE'))
# for key, value in dict1.items():
#     name, age, course = value
#     print ("{:<10} {:<10} {:<10}".format(name, age, course))


## Write a Python program to print a dictionary in table format.
## my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
## Sample Output:
## C1  C2  C3                                                                                                      
## 1   5   9                                                                                                         
## 2   6   10                                                                                                        
## 3   7   11

# mydict={'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# k=mydict.keys()
# v=mydict.values()
# print(k)
# print(v)

dict={'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
a,b,c=dict.keys()
print(a,b,c)
x,y,z=dict.values()
f=x,y,z
i=0
while i<len(f):
    print(x[i],y[i],z[i])
    i=i+1