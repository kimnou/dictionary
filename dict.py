# thisdict={"brand": "Ford","model": "Mustang","year": 1964}
# print(thisdict)



# thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
# print(thisdict["brand"])



# thisdict = {"brand": "Ford","model": "Mustang","year": 1964,"year": 2020}
# print(len(thisdict))



# thisdict = {"brand": "Ford","electric": False,"year": 1964,"colors": ["red", "white", "blue"]}
# print(thisdict)



# thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
# print(type(thisdict))


#==============access dictionaries=====================

# thisdict =	{"brand": "Ford","model": "Mustang","year": 1964}
# x = thisdict["model"]
# print(x)



##get method
# thisdict={"brand": "Ford","model": "Mustang","year": 1964}
# x=thisdict.get("model")
# print(x)



##get keys
# thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
# x = thisdict.keys()
# print(x)


# car={"brand": "Ford","model": "Mustang","year": 1964}
# x=car.keys()
# print(x)                    ##before the change
# car["color"] = "white"
# print(x)                    ##after the change


#=================get values==============
# car = {"brand": "Ford","model": "Mustang","year": 1964}
# x = car.values()
# print(x) #before the change
# car["year"] = 2020
# print(x) #after the change


# car = {"brand": "Ford","model": "Mustang","year": 1964}
# x = car.values()
# print(x) #before the change
# car["color"] = "red"
# print(x) #after the change


# car={"brand":"Ford","model":"Mustang","year":1964}
# x=car.items()
# print(x) #before the change
# car["year"] = 2020
# print(x) #after the change

##=========check if key exist===========
# thisdict={"brand":"Ford","model":"Mustang","year":1964}
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")

  
#===========nested=============
# myfamily={"child1":{"name":"Emil","year":2004},
#   "child2":{"name":"Tobias","year":2007},
#   "child3":{"name":"Linus","year":2011}}
# print(myfamily)



# child1={"name":"Emil","year":2004}
# child2={"name":"Tobias","year":2007}
# child3={"name":"Linus","year":2011}
# myfamily={"child1":child1,"child2":child2,"child3":child3}
# print(myfamily)