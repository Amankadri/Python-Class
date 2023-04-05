def menu():
    menu_display = """
    
                     Menu
              press 1 for addition
              press 2 for multiplication
            """
print(menu_display) 
choice = int(input("enter your choice :")) 
if choice==1:
   addition()   
else:
    pass

def addition():
    num1= int(input("Enter number 1"))
    num2= int(input("Enter number 2"))


    ans = num1 + num2
    print(ans)

menu()