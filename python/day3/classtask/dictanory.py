# set (not list)
mylist = {2, 4, 5, 3, 2, 34}
print("1."mylist)

# dictionary
dict1 = {"one": 1, "two": 2}

# access value using key
print(dict1["one"])

# print whole dictionary
print(dict1)

# dictionary keys
print(dict1.keys())

# dictionary values
print(dict1.values())

# dictionary items
print(dict1.items())

# dictonary update
dict2 = {"four": 4, "five": 5}
dict3 = {"six": 6, "seven": 7}
dict2.update(dict3)


# pop dictionhary item
dict3.pop
print(dict3)

# pop and remove the returns the last inserted values
dicta={"four": 4, "five": 5, "seven":7}
dicta.popitem()