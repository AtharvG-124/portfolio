'''class Parent:
    def __init__(self, fname, fage):
        self.name = fname
        self.age = fage

    def view(self):
        print(self.name, self.age)

class Child(Parent):
    def __init__(self, fname, fage):
        Parent.__init__(self, fname, fage)
        self.lastname = 'bob'

    def view(self):
        print(self.age, self.lastname, self.name)

ob = Child(23, 'python')
ob.view()'''
import random

options = ['rock', 'paper','scissors']
points = int(input("Number of points you want to play till: "))
computer_points = 0
player_points = 0

while player_points != points:
    player = input("choose: ")
    computer = random.choice(options)
    print("computer: ", computer, "\n")

    if (player == "scissors" and computer == "rock") or (player == "rock" and computer == "paper") or (player == "paper" and computer == "scissors"):
        computer_points += 1
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        player_points += 1

    print('You: ', player_points)
    print("Computer: ", computer_points, "\n")

    if computer_points == points:
        print("You lose")
        break
    elif player_points == points:
        print("Congratulations! You win")
