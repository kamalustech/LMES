var = "dhoni"
age = 42
# output = var + str(age)
# print(output)
#
# ##type cast  - string and int cant be added
#
# mail_contect = "Player " + var +""" is playing at age  """ + str(age)
# print(mail_contect)
#
# mail_content = f"Player {var} is playing at {age} "
# print(mail_content)

mail_content =  """Player {} is playing at age {}""".format(var, age)
print(mail_content)
