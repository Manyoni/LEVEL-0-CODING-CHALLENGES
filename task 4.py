def test_number_3 (x,y):
    total =x+y
    sum_list= list(str(total))
    #print(sum_list)
    if x == 3 or y == 3  or "3" in sum_list:
        return True
    else:
        return False

print(test_number_3(9,4))

