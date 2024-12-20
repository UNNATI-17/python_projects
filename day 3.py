print("Welcome to Treasure island.\n")

print("Your mission is to find the treasure\n")

dir=input('You are at a cross road. Where do you want to go? Type "left" or "right"\n')

if dir == "left":

    boat=input('You came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')

    if boat == "wait":

        door=input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n')

        if door == "yellow":

            print("congratulations! You found the treasure!!")

        else:
            print('game over')
    else:
        print('game over')
else:
    print('game over')



