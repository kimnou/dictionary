## Write a Python program to print all unique values in a dictionary. 
## Data:[{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},
## {"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
##Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

l=[{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
i=0
a=[]
while i<len(l):
    for j in l[i]:
        if l[i][j] not in a:
            a.append (l[i][j])
        i+=1
print(a)