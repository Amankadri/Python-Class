"""
function wuth return type and funvtion with parameters:

def funnname(parameters):
    return type
"""

def simpleinterest(p,n,r):
    si= p*n*r/100
    return si

p= int(input("Enter principle amount:"))    
n= int(input("Enter np of terms:"))    
r= int(input("Enter rate of interest:"))    

print(simpleinterest(p,n,r))