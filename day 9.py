logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the secret auction program.")
bids = {}
bidding_finished = True

def highest_bid(bidding_record):
    highest_bid_record = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = int(bidding_record[bidder])
        if bid_amount > highest_bid_record:
            highest_bid_record = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid_record}")

while bidding_finished:
    name = input("What is your name?")
    price = input("What is ur bid? $")
    bids[name] = price
    n = input("Are there any other bidders? Type 'yes' or 'no'.")
    if n == "no":
        bidding_finished =False
        highest_bid(bids)


