import random
from day14_1 import vs
from day14_1 import logo
from day14_1 import indian_personalities
def format_data(account):
    account_name = account["name"]
    account_title = account["title"]
    return f"{account_name}, a {account_title}"
def check_answer(user_guess,a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
print(logo)
score = 0
flag = True
account_b = random.choice(indian_personalities)

while flag:
    account_a = account_b
    account_b = random.choice(indian_personalities)

    
    if account_a == account_b:
        account_b = random.choice(indian_personalities)
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Comapre B: {format_data(account_b)}.") 
    guess = input("Who has more followers A or B?").lower()
    a_follower_count = account_a["instagram_followers"]
    b_follower_count = account_a["instagram_followers"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    if is_correct:
        score += 1 
        print(f"You are right! Current score {score}.")
        
        
    else:
        print(f"Sorry, that's wrong!!. Final score {score}.")
        flag = False
    





