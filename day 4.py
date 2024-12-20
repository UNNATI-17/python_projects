import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
n=int(input("What do u wanna choose? Type 0 for rocks, 1 for paper and 2 for scissors."))

if n == 0:
    print(rock)
if n == 1:
    print(paper)
if n == 2:
    print(scissors)
print("Computer Choose")
x=random_number=random.randint(0,2)
if x == 0:
    print(rock)
    if n == 2:
        print("you win")
    elif n == 1:
        print("you lose")
    else:
        print("it is a tie")
if x == 1:
    print(paper)
    if n == 0:
        print("you win")
    elif n == 2:
        print("you lose")
    else:
        print("it is a tie")
if x == 2:
    print(scissors)
    if n == 1:
        print("you win")
    elif n == 0:
        print("you lose")
    else:
        print("it is a tie")

        
