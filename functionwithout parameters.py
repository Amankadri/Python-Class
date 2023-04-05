"""
function without parameters and wuth retuen type

syntax:

def funnmae():
    return statement

"""    

def checkeliglible(age):
    if age>18:
        return "egligible for voting"
    else:
        return "not eligible for voting"   

print(checkeliglible(25))