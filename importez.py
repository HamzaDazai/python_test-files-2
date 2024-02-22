# Game 4,1
import gg 
import gint


print("Welcome to the Coin Guessing Game!")
input("Press Enter to start ....")
print("""Choose a method to toss the coin:
      1. Using random.random()
      2. Using random.randint()""")
choice_number = int(input("Enter your choice (1 or 2): "))
gss = gg
gsser = gint
if choice_number == 1:
    guess_choice = input("Enter your Guess (Heads or Tails): ").lower()
    if guess_choice == gss:
        print("You win")
    elif guess_choice != gss:
        print("Try again!")
else:
    print("ERROR")

if choice_number == 2:
    guess_choice = input("Enter your Guess (Heads or Tails): ").lower()
    if guess_choice == gsser:
        print("You win")
    elif guess_choice != gsser:
        print("Try agin")
else:
    print("ERROR")
