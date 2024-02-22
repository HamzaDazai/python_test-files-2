#random (MODEL) RANDOM is model choice number or anything random for you and calls them i your code by writing an (import random)
#using them .
import random
my_choise = random.randint (100,1000)
print(my_choise)
#randint (random intger ) it is using randint choices number random intger .


#يمكنك انشاء مدل مخصص عن طريق انشاء ملف اخر وكتابة متخيراة و الاوامر التي تريد استددعائها عن طريق كتابة اسم الملف كماهو مودح في الاسفل 
import gg
print (gg.hamza)
print (gg.dazia)


# example ;
import random
pin_code = random.randint(1000,9999)# HNA KALNA FE CODE IKHTAR RA9IM S7I7 MEN 1000 L 9999 3ASHWAAYAN 

user_pin = int(input("Enter a 4-digit PIN code: " ))#KALNA USER  idkhali code men 3ando fe 4 number 

if len(str(user_pin)) != 4 :# o hna kalna computer ichof sh7al men star kayn be stighdam (len) o shof wash feh 4 ar9am 
    print("ERRER!, Please enter 4 digits")
elif user_pin == pin_code:# hna kalna computer ichof wash ar9am li dakhilhom user wash kay sawi ar9am li khtarhom computer  
    print("Sucess PIN code matched")#ila tabi9sh chart tali3 had message
else:#hna kan kelo pc ila ma tab9osh had shorot kamlin tba3 hadshi fe print()
    print("Fallure! PIN code did not matsh")
    print(f"The computer generatedthis PIN: {pin_code}")


print("random heya metle  randint ida kant randint (random intger) faina random (random float")
float_user = random.random()
print(float_user)

#-----------------------------Data Structure--------------------------------
friends = ["Hamza","Moadh","adam","Ayoub","Simo"]
print(friends[0])  #result heya "hamza" ida ista3malna print
#append : ka zed fe list 
friends.append("ayman")#db ana zedt fe list smeyat "AYMAN" fe list
#extend : kat jma3 JOJ LIST M3A BA3DEYATO,
friends_b =["zaid","ikram","zenib","doua"]#ana zedt list jdeda
friends.extend(friends_b)
#remove : kat msa7 she7aja men list 
friends_b.remove("zaid")