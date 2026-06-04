var = "dhoni"
# print(var[0]) #it will start print from 0th index
# print(var[0:])# it will start printing from 0th index
# # print(var[0:2])#it will start from 0th index and end at 1st index
# print(var[-5])# dhon
# print(var[:7])# dhoni
# print(var[0:-3])

"""
0 - d - -5
1 - h - -4
2 - o - -3
3 - n - -2
4 - i - -1
string can be represented both in positive and negative index
picking up a particular set of data using its index is called "Slicing"
anything  before the : is starting index
anything after the : is the ending index

"""
# Python is a slow programming language since it operated in a sequence - line by line
# interpreter language
var = "india is a rich country"
print(var[::2])# oth index , last index, get me every 2nd data
print(var[::-2])# 0th index , last index, get me every 2nd data from reverse order
print(var[::-1])#reversing a string
print(var[::1])



