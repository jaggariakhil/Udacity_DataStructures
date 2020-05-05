def mergesort(items):
    # Base case
    if len(items) <= 1:
        return items

    # Find middle index of items
    mid = len(items) // 2

    # Create left list and right list
    left = items[:mid]
    right = items[mid:]

    # Recursively split lists again
    left = mergesort(left)
    right = mergesort(right)

    # Merge left list and right list
    return merge(left, right)


def merge(left, right):
    """
    Merges two lists
    :param left: Left list
    :param right: Right list
    :return: Merged list
    """
    merged = []
    left_index = 0
    right_index = 0

    # Iterate the two lists
    while left_index < len(left) and right_index < len(right):

        # If the first element in the right list is larger than the first element in the left list
        if right[right_index] > left[left_index]:

            # Append the first element in the right list
            merged.append(right[right_index])
            right_index += 1

        # If the first element in the left list is larger than the first element in the right list
        else:

            # Append the first element in the left list
            merged.append(left[left_index])
            left_index += 1

    # Add the rest of the (already sorted elements) of the other list
    # Note: Either the left list or the right list is already empty
    merged += left[left_index:]
    merged += right[right_index:]

    return merged


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
    input_list=mergesort(input_list)
    
    for i in range(length):
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





rearrange_digits([1, 2, 3, 4, 5])

        


