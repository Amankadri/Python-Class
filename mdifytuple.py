# modify tuple element


# note: tuple is immutable - but if we want to modify it we can convert it into list

t= (12,54,23,72)

l1=list(t)

l1.remove(23)


t= tuple(l1)
print(t)