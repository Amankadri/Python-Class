import random 

computer= random.randint(1,100)

status = True

while status:
    user= int(input("Enter the number :"))
    if user>computer:
        print(" HINT Guess lower number ")
    elif user<computer:
          print(" HINT Guess upper number ")  
    else:
        print("You got it")    
        status= False    