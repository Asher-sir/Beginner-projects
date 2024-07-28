
import random
r=random.randint(1,50)
print("hello welcome to the guess the number name")
a=int(input("please enter your guess "))
while(a!=r):
    if(a>r):
        print("your guess is higher")
        a=int(input("please enter your guess "))
    elif(a<r):
        print("your guess was low")
        a=int(input("please enter your guess "))
print('game ended')    


