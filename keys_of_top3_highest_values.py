# from heapq import nlargest
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}  
# three_largest = nlargest(3, my_dict, key=my_dict.get)
# print(three_largest)



dic={"a":50,"b":58,"c":56,"d":40,"e":100,"f":20}
a=sorted(dic.keys())
b=sorted(dic.values())
c=b[-3:]
d={}
for i in c:
    for j in a:
        if dic[j]==i:
            d[j]=i
y=[]
for x in d:
    y.append(x)
print(set(y))

# x=0
# y=0
# z=0
# k=[]
# for i in dic:
#     for j in dic:
#         if dic[j]>x:
#             x=dic[j]
#             a=j
#         elif dic[j]>y and dic[j]<x:
#             y=dic[j]
#             b=j
#         elif dic[j]>z and dic[j]<y:
#             z=dic[j]
#             c=j
# k.append(a)
# k.append(b)
# k.append(c)
# print(k)
# print(set(k))