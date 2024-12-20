import random

logo = ''' /  __// \ /\/  __// ___\/ ___\  /__ __\/ \ /|/  __/  / \  /|/ \ /\/ \__/|/  _ \/  __//  __\
| |  _| | |||  \  |    \|    \    / \  | |_|||  \    | |\ ||| | ||| |\/||| | //|  \  |  \/|
| |_//| \_/||  /_ \___ |\___ |    | |  | | |||  /_   | | \||| \_/|| |  ||| |_\\|  /_ |    /
\____\\____/\____\\____/\____/    \_/  \_/ \|\____\  \_/  \|\____/\_/  \|\____/\____\\_/\_\ '''

print(logo)
print('Welcome to the Number guessing game!')
print('I am thinking of a number between 1 and 100')


computer_number = random.randint(1, 101)
level_of_hardness = input("Choose a difficulty level. Type 'easy' or 'hard': ")

continue_game = True

def game():
    global continue_game
    user_guess = int(input("Make a guess: "))
    if computer_number == user_guess:
        print("You guessed it right!")
        continue_game = False
    elif computer_number > user_guess:
        print("Your guess is too low.")
    elif computer_number < user_guess:
        print("Your guess is too high.")

if level_of_hardness == "easy":
    user_score = 10
    print("You have 10 attempts to guess the number.")
elif level_of_hardness == "hard":
    user_score = 5
    print("You have 5 attempts to guess the number.")
else:
    print("Invalid difficulty level. Please restart the game and choose 'easy' or 'hard'.")
    continue_game = False  # Exit the game if invalid input


while continue_game and user_score > 0:
    game()
    if not continue_game:
        break
    user_score -= 1
    print(f"You have {user_score} attempts left to guess the number!")


if user_score == 0 and continue_game:
    print(f"You've run out of attempts! The correct number was {computer_number}. Better luck next time!")


    
        








