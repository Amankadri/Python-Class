status = True
while status:
    num = int(input("enter the number"))
    if num>=50:
     print("num is above 50")
    else:
     print("num is below 50")

    choice = input("do you want to continue press'y' for yes and press 'n' for no" )
    if choice=='y':
        status = True
    else:
        status = False    
        
