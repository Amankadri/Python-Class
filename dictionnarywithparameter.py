#normal function
def myfun(num1,num2,num3):
    sum = num1 +num2+num3
    print(sum)

myfun(12,24,34) 

#kwargs: key with arguments

# dictionary as a parameter

def myfun_dict(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}={v}")

myfun_dict(firstname="Anjali",lastname="patel",subject="python")