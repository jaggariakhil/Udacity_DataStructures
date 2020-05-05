def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list)==0:
        return []
    list1=[]
    list2=[]
    length=len(input_list)
    input_list.sort()
    
    for i in range(length-1,-1,-1):
        if i % 2 == 0:
            list1.append(str(input_list[i]))
        else:
            list2.append(str(input_list[i]))
    
    return [int(''.join(list1)), int(''.join(list2))]



def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])

test_function ([[4, 6, 2, 5, 9, 8], [964, 852]])

test_function ([[1,0,0,0,0,1,0,0,0], [10000, 1000]])

test_function ([[],[]])

test_function ([[9,7,6,5,2,3,3,2,2,1,8,9,3,3,5,1,0],[986533210, 97533221]])







        
