d = {}
usernames = []

name = input('First and Last name: ')
a = input("Username: ")
b = input("Password: ")


if a in usernames:
    print('username is already in use. Choose another')
else:
    d.update({'Name': name})
    d.update({'Username' : a})
    d.update({'Password': b})
usernames.append(a)
print(d)

