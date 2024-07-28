

import random#importing moudules
import string
length=int(input("enter the length of the password" ))

chlit=""

while(True):
    choice=int(input("enter the number 1 for letter,2 for number,3 for speacial and 4 for exit"))
    if(choice==1):#you can also do this with switch case but i decieded to do if else 
        chlit+=string.ascii_letters
    elif(choice==2):
        chlit+=string.digits
    elif(choice==3):
        chlit+= string.punctuation
    elif(choice==4):
        break
    else:
        print("please pick a valid option")
password="" 
for i in range(length):
    rchr=random.choice(chlit)
    password+=rchr#add the letter to the string 
    
print(password)
      