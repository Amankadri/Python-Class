#remove duplicate from the list 
#find unique element from the list

l1=["java","Android","java","php"]

l2=[]

for i in l1:
    if i not in l2:
        l2.append(i)

print(l2)        