# var = ["Kamal","Niralya", "Nithila"]
# print(var)
#
# var[0] = "Sherlin"#Mutable
# print(var)
#
# var = ["Kamal","Niralya", "Nithila"]
# var1 = var#Shallow Copy
# print(var1)
#
# var1[0] =  "Sherlin"
# print("Var1 " , var1)
# print("var ", var)

#
# var = ["Kamal","Niralya", "Nithila"]
# var1 = var[:]#deep Copy
# print(var1)
#
# var1[0] =  "Sherlin"
# print("Var1 " , var1)
# print("var ", var
#
#
# var = ["Dhoni","Kholi","Ashwin"]
# var.append("Raina")
# print(var)
#
# var = ["Dhoni","Kholi","Ashwin"]
# var.insert(2,"Raina")
# print(var)

# var = ["Dhoni","Kholi","Ashwin"]
# var[1]= "Raina"
# print(var)

# var = ["dhoni", "Kholi","Stewart"]
# data_index = var.index("Kholi")
# print(data_index)
# var[data_index] = "Saina"
# print(var)
#

# var = ["Dhoni","Kholi","Saina","Kholi","Daina","Kholi"]
# for index, data in enumerate(var):
#     print(index)
#     if data == "Kholi":
#         var[index] = "Raina"
# print(var)

# var = ["Dhoni","Kholi","Saina","Kholi","Daina","Kholi"]
# for index, data in enumerate(var):
#     if data == "Kholi":
#         print(index)
# var[index] = 'Kamal'
# print(var)
#
# var = ["dhoni","Kholi",'ashwin']
# var.pop()
# print(var)

# var = ["dhoni","Kholi",'ashwin']
# var.remove("ashwin")
# print(var)
#


# var = ["dhoni","Kholi",'ashwin']
# var.clear()
# print(var)
#
#
# var = ["dhoni","Kholi",'ashwin']
# del var
# print(var)

# var = [0,1,2,3,4,5,6,7,8,9,10]
# for x in var:
#     if x % 2 == 0:
#         print(x)

# var = [0,1,2,3,4,5,6,7,8,9,10]
# output = []
# for x in var:
#     if x % 2 == 0:
#         output.append(x)
# print(output)

# var = [0,1,2,3,4,5,6,7,8,9,10]
# output = [x for x in var if x % 2 == 0] #list comprehension
# print(output)
#
# var = ["dhoni","kholi",'ashwin']
# var.sort()
# print(var)

#
# var = ["dhoni","kholi",'ashwin']
# print(var.sort(reverse=True)) #Sort method on a variable returns nothing
# print(var)

#
# var = ["dhoni","kholi",'ashwin']
# print(sorted(var))#will return data
# print(var)


# var = ["dhoni","kholi",'ashwin','ak']
# print(sorted(var,reverse=True))#will return data
# # print(var)


#
# var = ["dhoni","kholi",'ashwin','ak']
# print(sorted(var,key=len))#will return data
# # print(var)


#
# var = ["dhoni","kholi",'ashwin','ak']
# output = var[::-1]
# print(output)

# var = ["Dhoni","Kholi","Saina","Kholi","Daina","Kholi", "Kokki"]
# lastindex = len(var) - 1 - var[::-1].index("Kholi")
#
# print(lastindex)
# var[lastindex] = 'Bunny'
# print(var)

var = ["Dhoni","Kholi","Saina","Kholi","Daina","Kholi", "Kokki"]
var[len(var) - 1 -var[::-1].index("Kholi")] = "Rambo"
print(var)