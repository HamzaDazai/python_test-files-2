# Game 4,1
import random


print("Welcome to the Coin Guessing Game!")
input("Press Enter to start ....")
print("""Choose a method to toss the coin:
      1. Using random.random()
      2. Using random.randint()""")
choice_number = int(input("Enter your choice (1 or 2): "))
if choice_number == 1:
    random_number = random.random()
    if random_number >= 0.5:
        computer_result = "Heads"
    else:
        computer_result = "Tails"
elif choice_number == 2:
    if random.randint(0,1) == 0:
        computer_result = "Heads"
    else:
        computer_result = "Tails"
else:
    print("Invalid choice . Please select either 1 or 2")

guess_choice = input("Enter your Guess (Heads or Tails): ").lower()
if guess_choice == computer_result.lower():
    print("You win")
else:
    print("try again")

print(f"The computer choice is {computer_result}")