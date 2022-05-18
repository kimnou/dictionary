### output== {“one”:1,”two”:2,”three”:3,”four”:4,”five”:5}

# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5]
# new_dict={}
# l=len(list1)
# i=0
# while i<l:
#     new_dict[list1[i]]=list2[i]
#     i+=1
# print(new_dict)

# for i in range(l):
#     new_dict[list1[i]]=list2[i]
# print(new_dict)

list=['one','two','three','four','five']
i=1
a=[]
while i<=len(list):
    a.append(i)
    x={}
    y={}
    j=0
    k=0
    while j<len(a) and k<len(list):
        y[list[k]]=a[j]
        x['numbers']=y
        j+=1
        k+=1
    i+=1
print(x)