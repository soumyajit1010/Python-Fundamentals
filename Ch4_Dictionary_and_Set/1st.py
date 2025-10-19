info = {
    "name" : "ApnaCollege",
    "learning" : "codingInPython",
    "topics" : ("dict", "set"),
    "age" : 35,
    "isAdult" : True,
    "marks" : 94.4,
    True : "aaaa",
    12 : "xxxx"
}

print(info)
print(type(info))

print(info["name"])
print(info["topics"])
print(info[12])

info["name"] = "Soumyajit_Rout"
print(info)
info["xxxx"] = "1234"
print(info)


nullDict = {}
print(nullDict)
nullDict["ex1"] = "Sneha"
print(nullDict)