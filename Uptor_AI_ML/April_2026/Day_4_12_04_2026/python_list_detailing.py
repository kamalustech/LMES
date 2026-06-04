var = [2,4,5,7,8]
# print(var)
# print(type(var))
# sum = 0
# for x in var:
#     # print(x)
#     sum = sum + x
# print(sum)

# Python list is not an array by default
import numpy
var = [2,3,4,5,6,7]
# var_arry = numpy.array(var)
# print(var_arry)
# print(type(var_arry))
#
# # numpy - numerical python - user for easy numerical calulations
# sum = var_arry.sum()
# print(sum)

# import numpy as np
# car_arry = np.array([2,3,4,5,6,7]).sum()
# print(car_arry)
# var_array = np.array([2,3,4,5,6,7,8]).sum()
# print(var_array)

var = [2,0,3,4,5,6,7,8]
sum = 0
for x in var:
    if  x%2 == 0:
        sum = sum + x
        break
    else:
        print("odd number" + str(x))
        # break
print(sum)