status= True

sum= 0
while status:
    num = int(input("enter the number"))
    sum = +num
  

    choice = input("do you want to continue press'y' for yes and press 'n' for no" )
    if choice=='y':
        status = True
    else:
        status = False    

print("total = ",sum)