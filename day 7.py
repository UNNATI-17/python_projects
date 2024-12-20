import random

from day7_1 import word_list
from day7_1 import stages
from day7_1 import logo

end_of_game = False
print(logo)
choose_word = random.choice(word_list)

lives = 6
display = []
word_length = len(choose_word)
for letter in range(word_length):
    display.append("_")
 
print(display)


while not end_of_game:

    guess = input("Guess a letter!").lower()

    if guess in display:
         print(f"You've already guessed {guess}")
         
    for position in range(word_length):
        
    
        letter = choose_word[position]
        if letter == guess:
            display[position]=letter
    if guess not in choose_word:
           print(f"You guessed {guess}, that's not in the word. You lose a life.")
           lives -= 1
           if lives == 0:
                end_of_game = True
                print("You lose.")
                print(f"The right word is {choose_word}, Better luck next time")
    

    print(display)
    if "_" not in display:
        end_of_game = True
        print("Congratulaions, You won the game!!!!")
    print(stages[lives])

    


