# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)


# my_dict=()
# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# my_dict=my_dict+(dic1,)
# my_dict=my_dict+(dic2,)
# my_dict=my_dict+(dic3,)
# print(my_dict)


# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# dicts = dic1, dic2, dic3
# print(dicts)



# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# dicts=[]
# dicts.append(dic1)
# dicts.append(dic2)
# dicts.append(dic3)
# print(dicts)



# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# dict = {}
# dict.update(dic1)
# dict.update(dic2)
# dict.update(dic3)
# print(dict)


dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
for i in dic1:
    if i in dic2:
        dic2[i]=dic1[i]+dic2[i]
dic1.update(dic2)
dic1.update(dic3)
print(dic1)


    