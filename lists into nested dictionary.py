## Write a Python program to convert more than one list to nested dictionary. 
## Original strings:
## ['S001', 'S002', 'S003', 'S004']
## ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
## [85, 98, 89, 92]
## Nested dictionary:
## [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]


list1=['S001', 'S002', 'S003', 'S004']
list2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
list3=[85, 98, 89, 92]
x=[{a:b} for a,b in zip(list2,list3)]
y=[{c:d} for c,d in zip(list1,x)]
print(y)



