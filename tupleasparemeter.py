"""
tuple as parametr

and 

dictionary as a parameter

----------------------------------
*args & **kwargs

args : arguments
kwargs: key with arguments

"""

#normal function
def myfun(num1,num2,num3):
    sum = num1 +num2+num3
    print(sum)

myfun(12,24,34)   

#args : tuple as a parameter - we can pass no of paramters

def myfun_args(*args):
    sum = 0
    for i in args:
        sum+=i
    print(sum)    
