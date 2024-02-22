#funddd 
import random 

print("Welcome to the Goin Guessing Game !")
input("Press Enter to start ....")
print("""choose a method to toss the coin:
      1. Using random.random()
      2. Using random.randint()""")
choice_number = int(input("Enter your choice (1 or 2 ): "))
if choice_number == 1:
    random_number = random.random()
    if random_number >= 0.5:
        computer_result = "Heads"
    else:
        computer_result = "Tails"
elif choice_number == 2:
    random_number = random.randint(0,1)
    if random_number == 0:
        computer_result = "Heads"
    else:
        computer_result = "Tails"
else:
    print("Invalid choice. Please select either (1 or 2) ")

guess_choice = input("Enter your Guess (heads or Tails): ").lower()
if computer_result == guess_choice:
    print("good job, you win ")
else:
    print("we soory about that, you losse hhhhhhhhhhhhh")

print(f"the computer choise is {computer_result} and your choise is {guess_choice}")