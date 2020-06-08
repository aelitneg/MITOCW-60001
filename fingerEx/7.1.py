# Finger exercise: Implement a function that meets the specification 
# below. Use a try-except block. def sumDigits(s): 

def decimalDigitSum(s):
    """
    Assumes s is a string Returns the sum of the decimal digits 
    in s For example, if s is 'a2b3c' it returns 5
    """

    sum = 0
    for v in s:
        try:
            sum += int(v)
        except ValueError:
            continue
    
    return sum

print(decimalDigitSum('a2b3c'))
