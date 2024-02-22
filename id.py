contry = input(" are you moroccan ? (yes/no) : ")
if contry.lower() == "yes":
    age = input("how old are you ?")
    if age >= "18":
        print("you can use id cart ")
    else:
        print("you can not use id cart")
else:
    print("if you not moroccan you can't use this exparice")