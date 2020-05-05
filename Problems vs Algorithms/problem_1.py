def recu_sqrt(mid,number):
    mid=mid
    result1=mid**2
    result2=(mid+1)**2
    
    if result1==number:
        return mid 
    elif result1<number and result2>number:
        return mid
    elif result1>number:
        return recu_sqrt(mid-1,number)
    else:
        return recu_sqrt(mid+1,number)
    

    
       
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if(number<0):
        return None
    low=0
    high=number
    mid=low+high//2
    return recu_sqrt(mid,number)
    

print ("Pass" if  (3 == sqrt(9)) else "Fail")   # Pass
print ("Pass" if  (0 == sqrt(0)) else "Fail")   # Pass
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

print ("Pass" if  (6 == sqrt(36)) else "Fail")
print ("Pass" if  (12 == sqrt(-144)) else "Fail")

print ("Pass" if  (5 == sqrt(27.99)) else "Fail")


print ("Pass" if  (15 == sqrt(255.5)) else "Fail")
