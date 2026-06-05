# var = dict()
# print(type(var))
#
# var = {}
# print(type(var))
#
# var = {"dhoni","csk",42}
# print(type(var))
# var = {"name":"dhoni","team":"csk","age":42}
# print(type(var))

"""Dictionary
1. Dictionary is called key value pair
2. Name : data (anything before: is key and anything after : is value)
3. Dictionary wont work directly with indexing
4. just becuse it is working based on key
5. Dictionary is called hash table
6. anything we store in form of key is called hashing
7. dictionay key can be of any immutable type (eg:: str, num, tuple ) but not list
8. dictionary should not be duplicated
9. if duplicated it will pick the latest declared dictionary
"""
from idlelib import outwin

#print(var[0]) # this line will throw error becasue dictionary cannot be manupulated using index
# dictionary is easily accessible than index
# var = {"name":"dhoni",('a',"b"):"csk","age":42, True:"Kamal"}
# print(type(('a',"b")))
# print(var[('a',"b")])
# var["Country"] = "India"
# print(var)
# var["Country"] = 'Nepal'
# print(var)
# #dictionary is mutable
#
var = {"name": "dhoni","country":["Burma"]}
# print(var)
var["country"].append("India")
# print(var)
# var["country"].extend(["Singapore","Japan"])
# print(var)
# print(type(var["country"]))

# print(var["country"][0])
# print(type(var["country"][0][0])) #Chained indexing

# var = {"name":"dhoni", "country":["australia","Denmark","Cuba"]}
# var1 = {"team":"csk"}
# print(var + var1)

# var = {"name":"dhoni", "country":["australia","Denmark","Cuba"]}
# var1 = {"team":"csk"}
# var.update(var1)
# print(var)

# var = {"name":"dhoni", "country":["australia","Denmark","Cuba"]}
# var1 = {"team":"csk"}
# var2 = {"age":42}
# output = {**var,**var2,**var1}
# print(output)
#
import json
var = '{"name":"dhoni","team":"rcb","team":"csk"}'
# # print(type(var))
# # print(tuple(var))
# # print(var)
# print(var[0])
# # print(var["name"])
# convert_var = json.loads(var)
# print(type(convert_var))
#
# # var = str(convert_var)
# # print(var)
# converted_str = json.dumps(var)
# print(type(converted_str))
#
# print(var["team"])

var = {"name":"dhoni","team":"rcb","team":"csk"}
for x in var:
    print(x)

for x in var.items():
    print(x)
for key,values in var.items():
    print(key,values)

for value in var.values():
    print(value)

for key in var.keys():
    print(key)

