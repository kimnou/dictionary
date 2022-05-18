# dict={'a':[1,2,3,4],'b':['a','b','c','d']}
# a=[]
# b=[]
# y=[]
# for i in dict:
#     b.append(i)
#     a.append(dict[i])
#     i=0
#     while i<len(a):
#         j=-1
#         x=[]
#         while j>=-len(a[i]):
#             x.append(a[i][j])
#             j-=1
#         i+=1
#     y.append(x)
# z={}
# for i in range(len(b)):
#     z[b[i]]=y[i]
# print(z)


dict={'a':[1,2,3,4],'b':['a','b','c','d']}
for i in dict:
    x=dict[i]
    j=-1
    b=[]
    while j>=-len(x):
        b.append(x[j])
        j-=1
    dict[i]=b
print(dict)
