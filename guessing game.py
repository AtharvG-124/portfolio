import random
n = 20
secret_number = int(n * random.random()) + 1
guess = 0
while guess != secret_number:
    guess = int(input("New Number = "))
    if guess > secret_number:
        print("The number is too big")
    else:
        print("The number is too small")
else:
    print("Yay! You guessed it!")

'''
a = lambda x: x*x
end = 0

print("If you want to exit the calculator, then press 0")
while True:
    s = float(input("Number: "))
    print("result", a(s))
    if s == end:
        print("Thank You")
        break
'''

