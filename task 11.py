def printing_common_characters(str1,str2):
    a = list(set(str1)&set(str2))
    characters_list =[]
    character=0

    for i in a:
         character = character+1
         characters_list.append(i)
    print (characters_list)

printing_common_characters("house","computer")


