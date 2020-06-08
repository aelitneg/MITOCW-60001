# Finger Exercise: Implement a function that satisfies the specification 

def findAnEven(L): 
    """
    Assumes L is a list of integers Returns the first even number 
    in L Raises ValueError if L does not contain an even number
    """
    for v in L:
        if (v % 2 == 0):
            return v
    raise ValueError("findAnEven list contained no evens")

nums = [1, 3, 5]

print("Even:", findAnEven(nums))
