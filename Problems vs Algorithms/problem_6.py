def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints)==0:
        return None
    minvalue=None
    maxvalue=None
    for i in ints:
        if minvalue == None :
            minvalue = i
        elif i < minvalue:    
            minvalue=i
        if maxvalue == None :
            maxvalue = i
        elif i > maxvalue:
            maxvalue = i
    return(minvalue,maxvalue)         

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "FaiL")



l = []  # An empty list
print("Pass:\nList: " + str(l) + "\n(min, max): " + str(get_min_max(l)) if (None is get_min_max(l)) else "Fail")
print()

l = [1]  # An list with one element
print("Pass:\nList: " + str(l) + "\n(min, max): " + str(get_min_max(l)) if ((1, 1) == get_min_max(l)) else "Fail")
print()

l = [i for i in range(0, 10)]  # A list containing 0 to 9
random.shuffle(l)
print("Pass:\nList: " + str(l) + "\n(min, max): " + str(get_min_max(l)) if ((0, 9) == get_min_max(l)) else "Fail")
print()

l = [i for i in range(-12, 25)]  # a list containing -12 to 24
random.shuffle(l)
print("Pass:\nList: " + str(l) + "\n(min, max): " + str(get_min_max(l)) if ((-12, 24) == get_min_max(l)) else "Fail")
print()

l = [i for i in range(-24, -1)]  # a list containing -24 to -2
random.shuffle(l)
print("Pass:\nList: " + str(l) + "\n(min, max): " + str(get_min_max(l)) if ((-24, -2) == get_min_max(l)) else "Fail")
print()

l=[12,35,2827,82,3838,-75647,7272,74,0,2828,282,12,90,-19,20,-202,-890]
random.shuffle(l)
print("Pass:\nList: " + str(l) + "\n(min, max): " + str(get_min_max(l)) if ((-75647, 7272) == get_min_max(l)) else "Fail")
print()
