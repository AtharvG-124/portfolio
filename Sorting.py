import random

a = []
for i in range(23):
    b = random.randrange(100)
    a.append(b)
a.sort()
print(a)
num = int(input('number: '))

l = len(a)

start = a[0]
mid = a[l//2]
end = a[l - 1]
x = l - 1
flag = False

for i in range(l):
    c = x // 2
    d = c//2
    if num > mid:
        mid = a[(x - d) // 2]
        start = mid
        if mid == num:
            flag = True
            break
    elif num < mid:
        end = a[c]
        mid = a[d]
        print(mid)
        if mid == num:
            flag = True
            break
print(flag)