def printing_common_characters(str1,str2):
    a = list(set(str1)&set(str2))
    string =""   
    for i in a:
        string +=i
    return string
    

a = printing_common_characters("house","computer")
print ("Common letters:",a)








