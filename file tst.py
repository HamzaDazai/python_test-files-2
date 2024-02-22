import random
print("Welcome to 'whose wallet ?'")
names = input("""You will give me list names, and I will pick a person to pay 
              If you're ready , enter the names separated by a comma : """)
finl_names = names.split(", ")
h_names = random.choice(finl_names)
print(f"the  person hi will pay is {h_names}")