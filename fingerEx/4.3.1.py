# Finger exercise: When the implementation of fib in Figure 4.7 
# is used to compute fib(5), how many times does it compute the 
# value of fib(2) on the way to computing fib(5)?

def fib(n): 
    """
    Assumes n int >= 0
    Returns Fibonacci of n
    """

    if n == 0 or n == 1:
        return 1
    else:
        if (n == 2):
            print("fib(2)")
        return fib(n -1) + fib(n - 2)

fib(5)
