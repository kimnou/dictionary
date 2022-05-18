# d={'bijender':45,'deepak':60,'param':20,"anjili":30,'roshini':50}
# p=sorted(d.values())
# print(p)
# a={}
# for i in p:
#     for j in d.keys():
#         if d[j]==i:
#             a[j]=i
# print(a)



# d={'bijender':45,'deepak':60,'param':20,"anjili":30,'roshini':50}
# p=sorted(d.values())
# a={}
# for i in reversed(p):
#     for j in reversed(d.keys()):
#         if d[j]==i:
#             a[j]=i                                                                                                                                                                                                                                                                                                                                                                                                                                         
# print(a)

name={'bijender':45,'deepak':60,'param':20,"anjili":30,'roshini':50}
for i in name:
    for j in name:
        if name[j]>name[i]:
            name[j],name[i]=name[i],name[j]
        elif name[i]>name[j]:
            name[j],name[i]=name[i],name[j]
print(name)