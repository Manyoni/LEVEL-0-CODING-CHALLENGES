def return_maximum_number(x,y,z):
    if (x >=y) and (x >=z):
        maximum = x
    elif (y >=x) and (y >= z):
        maximum =y
    else:
        maximum =z
    return maximum

a =10
b =40
c =97

calling_the_function = return_maximum_number(a,b,c)
print (calling_the_function)

