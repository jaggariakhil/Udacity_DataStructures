def rotated_array_search(input_list  , number ):
    """
    Find the index by searching in a rotated sorted array
    Args:
       input_list(list): Input array to search
       number(int): Target to search for
    Returns:
       int: Index or -1
    """

    return binarysearch(input_list, number, 0, len(input_list) - 1)




def binarysearch( ip , target , low , high ):
    if low > high:
        return -1

    mid = (low + high) // 2
    
    if target == ip[ mid ]:
        return mid

    
    ls = binarysearch( ip , target , low , mid - 1)

    
    rs = binarysearch( ip , target, mid + 1 , high )

   
    return max(ls, rs)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

    print("input_list:", input_list)
    print("number:", number)
    print("linear_search(input_list, number):", linear_search(input_list, number))
    print("rotated_array_search(input_list, number)", rotated_array_search(input_list, number))
    print()


test_function([[], 0])
test_function([[0, 1, 2, 3, 4, 5], 5])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])



test_function([[12,13,14,15,16,17,1,2,3,4,5,6,7,8,9,10,11],16])
test_function([[12,13,14,15,16,17,1,2,3,4,5,6,7,8,9,10,11],11])
test_function([[12,13,14,15,16,17,1,2,3,4,5,6,7,8,9,10,11],14])
test_function([[12,13,14,15,16,17,1,2,3,4,5,6,7,8,9,10,11],28])


test_function([[24,25,26,27,28,29,30,18,19,20,21,22,23],22])
test_function([[24,25,26,27,28,29,30,18,19,20,21,22,23],1])

test_function([[24,25,26,27,28,29,30,18,19,20,21,22,23],101])


