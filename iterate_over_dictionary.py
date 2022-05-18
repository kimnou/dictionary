## Write a Python program to iterate over dictionaries using for loops.


# dict={"vocal":"jisoo","mainvocal":"rose","rapper":"jennie","dancer":"lisa"}
# for i in dict:
#     print(i)


# dict={"vocal":"jisoo","mainvocal":"rose","rapper":"jennie","dancer":"lisa"}
# for i in dict:
#     print(dict[i])



# dict={"vocal":"jisoo","mainvocal":"rose","rapper":"jennie","dancer":"lisa"}
# for i in dict:
#     print(i,dict[i])



dict={"vocal":"jisoo","mainvocal":"rose","rapper":"jennie","dancer":"lisa"}
for i,j in dict.items():
    print(i,j)