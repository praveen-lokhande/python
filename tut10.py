#Dictionary is nothing but key value pairs
d1={"harry":"burger","praveen":"eggrice","prateek":"noodels"}
print(type(d1))
print(d1["prateek"])
d1["aditya"]="vimal"
print(d1)
d1["dhiraj"]={"a":"pizza","b":"biriyani","c":"vodapav"}
print(d1["dhiraj"]["a"])
del d1["dhiraj"]
print(d1)

d2=d1.copy()
print(d2)

del d2["aditya"]
print(d1)
print(d2)

#Dictonary functions
d1.update({"dhiraj":"pizza","sushil":"egg"})
print(d1)
print(d1.get("dhiraj"))
print(d1.keys())
print(d1.items())
print(d1.values())