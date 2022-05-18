## Write a Python program to get the top three items in a shop.
## data:{'item1':45.50,'item2':35,'item3':41.30,'item4':55,'item5':24}
## Expected Output:
## item4 55
## item1 45.5
## item3 41.3

dict={'item1':45.50,'item2':35,'item3':41.30,'item4':55,'item5':24}
a=0
b=0
c=0
for i in dict:
    for j in dict:
        if dict[j]>a:
            a=dict[j]
        elif dict[j]>b and dict[j]<a:
            b=dict[j]
        elif dict[j]>c and dict[j]<b:
            c=dict[j]
print(a,b,c)
    

