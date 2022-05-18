# a={"a":10,"b":20,"c":5}
# b={"a":50,"b":10,"c":5}
# for i in a:
#     b[i]=a[i]+b[i]
# # a.update(b)
# print(b)



# a=input("enter key:")
# b=input("enter value")
# dict={}
# dict[a]=b
# print(dict)



# dict={'a':10,'b':5,'c':20,'d':15}
# a=input("enter key:")
# b=int(input("enter value:"))
# for i in dict:
#     if a==i:
#         dict[i]=dict[i]-b
# print(dict)



# dict={'a':"dict",'b':"twenty",'c':"navgurukul",'d':"wednesday"}
# user=input("enter input:")
# for i in dict:
#     if user==dict[i]:
#         print(i)
#     elif user==i:
#         print(dict[i])


# dict={'a':10,'b':5,'c':20,'d':15}
# a=input("enter first key:")
# b=input("enter second key:")
# dict1=0
# for i in dict:
#     if a==i:
#         dict1=dict[a]-dict[b]
# print(dict1)


# i=0
# while i<10:
#     i+=1
#     if i==2 or i==5:
#         continue
#     print(i) 
# 

# i=0
# while i<10:
#     i+=1
#     if i==5:
#         break
#     print(i) 
# 
#
#  num=int(input("enter number:"))
# if num>0:
#     print(-num)
# else:
#     print(-num) 


# a=5
# b=6
# c=-a-b
# print(-c)


# num=int(input("enter number:"))
# a={}
# for i in range (1,num+1):
#     a[i]=i*i
# print(a)


##swapping
# a=6
# b=5
# c=b
# b=a
# a=c
# print(b,a)

# a=5
# b=6
# b,a=a,b
# print(b,a)



# a=[1,4,5,9]
# i=0
# b=[]
# while i<len(a):
#     i+=1
# b.append(a[-1]+1)
# a.extend(b)
# print(a)



#op=kAgUilE
#[1,3,6] KGL
# a="KaGuILe"
# i=0
# while i<len(a):
#     if a[i].islower():
#         print(a[i].upper(),end="")
#     else:
#         print(a[i].lower(),end="")
#     i+=1

# a="KaGuILe"
# i=0
# b=[]
# while i<len(a):
#     if a[i].isupper():
#         b.append(i)
#     i+=1
# print(b)

# a="KaGuILe"
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if a[i].islower():
#         c.append(a[i].upper())
#         d="".join(c)
#     else:
#         c.append(a[i].lower())
#         d="".join(c)
#     i+=1
# print(d)
# j=0
# x=[]
# while j<len(d):
#     if d[j].isupper():
#         x.append(j)
#     j+=1
# print(x)

# a=[0,2,7,4,5]
# b=[]
# n=int(input("enter index number:"))
# for i in range(n):
#     b.append(a[i])
# print(b)

# a=[0,2,7,4,5]
# b=[]
# n=int(input("enter index number:"))
# if n>len(a) and n==10:
#     print(a)
# elif n>len(a) and n!=10:
#     print(b)
# else:
#     for i in range(n):
#         b.append(a[i])
#     print(b)

