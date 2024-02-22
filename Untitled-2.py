#sumble
print("""░░░░░░░░░░░║
░░▄█▀▄░░░░░║░░░░░░▄▀▄▄
░░░░░░▀▄░░░║░░░░▄▀
░▄▄▄░░░░█▄▄▄▄▄▄█░░░░▄▄▄
▀░░░▀█░█▀░░▐▌░░▀█░█▀░░░▀
░░░░░░██░░▀▐▌▀░░██
░▄█▀▀▀████████████▀▀▀█
█░░░░░░██████████░░░░░▀▄
█▄░░░█▀░░▀▀▀▀▀▀░░▀█░░░▄█
░▀█░░░█░░░░░░░░░░█░░░█▀
""")
#messge hello
print("Welcome to my islande")
#choise door
doors = input("There are two doors in front of you. 🚪 a red door and 🚪 a blue door ").lower()
if doors == "red door":
    print("Great! now you entered a room.")
    boxes = input("You found three boxes : 🎁 white, 🎁 black, 🎁 green.").lower()
    if boxes ==  "white":
        print("GAME OVER, this 🎁 box It contains toxic gas ☢☢☢☢")
    elif boxes == "balck" :
        print("You diea, this box It contains ⚡⚡⚡")
    elif boxes == "green":
        print("Congratulations! You found the treasure 💰💰💰")
    else:
        print(" are you chore you choise the option (white / black / green)? ")
elif doors == " blue door":
    print("Nop this is ronge doore baybe hhhhh")
else :
    print(" you chore choise the option (red door / blue door )")