#from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
end_auction = False
bidders = {}
max_bid = 0
winner = ""
print("Welcom to the secret auction program.")
while not end_auction:
  name = input("What is your name?:\n ")
  bid_price = int(input("What is your bid?/\n"))
  bidders[name] = bid_price
  bid_again = input("Are there any other bidders? Type 'yes' or 'no' ")
 # clear()
  if bid_again == 'no':
    for name in bidders:
      if bidders[name] > max_bid:
        max_bid = bidders[name]
        winner = name
    print(f"the highest bidder is {winner}")
    break

