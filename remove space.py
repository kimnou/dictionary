## Write a Python program to remove spaces from dictionary keys.
## Original dictionary:  {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
## New dictionary:  {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']}


dic={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
mydic={}
for i in dic:
    d={i.replace(" ","")}
    for j in d:
        mydic[j]=dic[i]
print(mydic)
