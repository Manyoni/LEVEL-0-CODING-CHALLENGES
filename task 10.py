def printing_vowels(str):
    vowels=0
    vowels_list =[]
    for i in str:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels +=1
            vowels_list.append(i)
    print (vowels_list)
    








