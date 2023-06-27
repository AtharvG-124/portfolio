import random
a = []
for i in range(20):
    b = random.randrange(100)
    a.append(b)
a.sort()
print(a)
l = len(a)
num = int(input('number: '))

flag = False
for i in range(l):
    print(a[i])
    if a[i] == num:
        flag = True
        break
    elif a[i] > num:
        break
print(flag)