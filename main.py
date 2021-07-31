from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
bids ={}
game = True
highest_bid=0
highest_player=""
while game:
  name = input("What's your name? ")
  bid = input("What's your bid? ")  
  bids[name] = bid
  others = input("is the other users who wants to bid? Y or N ")
  if others.lower() == "y":
    clear()
  else:
    for names in bids:
      value = int(bids[names])
      if value > highest_bid:
        highest_player = names
        highest_bid = value
    game=False

print(f'{highest_player} won with a bid of {highest_bid}')