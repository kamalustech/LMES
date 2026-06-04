from idlelib import outwin
var = ['dhoni','ashwin', 'rahul',5,2,5,1,8]
# str_var = [x for x in var if isinstance(x, str)]
# num_var = [y for y in var if isinstance(y, int)]

# for x in var:
#     if isinstance(x, str):
#         str_var.append(x)
#     elif isinstance(x, int):
#         num_var.append(x)

# str_reversal = []

# str_reversal = [y[::-1] for y in sorted([x for x in var if isinstance(x, str)])] #List Comprehension

# output = sorted(num_var) + str_reversal
output = [y[::-1] for y in sorted([x for x in var if isinstance(x, str)])] + [y for y in var if isinstance(y, int)]
print(output)

print([y[::-1] for y in sorted([x for x in var if isinstance(x, str)])] + [y for y in var if isinstance(y, int)]
)