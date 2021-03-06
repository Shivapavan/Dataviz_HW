names = []
for _ in range(5):
    name = input("Please enter the name of someone you know. ")
    names.append(name)

# @TODO: Use a list comprehension to create a list of lowercased names
lcase = [lcase.lower() for lcase in names]
print(lcase)
#for name in names:
    #lcase.append(name.lower())

# @TODO: Use a list comprehension to create a list of titlecased names
# https://www.tutorialspoint.com/python/string_title.htm
titlecased = [titlecased.title() for titlecased in names]
#for name in names:
    #titlecased.append(name.title())

invitations = [f"Dear {name}, please come to the wedding this Saturday!" for name in titlecased]

for invitation in invitations:
    print(invitation)