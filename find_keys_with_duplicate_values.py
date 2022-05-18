dic={"ball":4,"bat":4,"wickets":8,"ball":"green","bat":3}
a_list = []
for k,v in  dic.items():
    if v in dic.values() and v != dic.keys():
        a_list.append(k)
print(a_list)
# v=dic.values()
# print(v)
# # for i in dic:

# #     if i not in my_dict:
# #         my_dict[i]=dic[i]
# # print(my_dict)
