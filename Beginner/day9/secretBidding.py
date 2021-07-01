from art import logo
# from replit import clear

print(logo)


def bidding(bidder_name, bidding_price):
    bids[bidder_name] = bidding_price


def check_winner(bidding_record):
    winner = ""
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bidding_record[bidder]
            winner = bidder
    print(f"The Winner in the Bid is {winner} with bid {highest_bid}")


bids = {}
is_bidding_end = False
while not is_bidding_end:
    name = input("What's your name? \n")
    bid = int(input("Enter your bidding value \n $"))
    bidding(bidder_name=name, bidding_price=bid)
    should_continue = input("Do you have any other bids? 'Yes' or 'No' \n").lower()
    if should_continue == "no":
        is_bidding_end = True
        check_winner(bids)
    else:
        print("Clear")

