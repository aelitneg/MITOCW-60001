# Finger exercise: Add some code to the implementation of Newton-Raphson
#  that keeps track of the number of iterations used to find the root.
#  Use that code as part of a program that compares the efficiency 
# of Newton-Raphson and bisection search. (You should discover that 
# Newton-Raphson is more efficient.)

epsilon = 0.01
k = 24.0
guess = k/2.0
iterations = 0
while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) -k)/(2*guess))
    iterations = iterations + 1
print('Newton-Raphson Root:', guess)
print('Iterations', iterations)

x = 24
epsilon = 0.01
iterations = 0
low = min(0, x)
high = max(1.0, x)
ans = (high + low) / 2
while abs(ans**2 - x) >= epsilon:
    iterations += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = ( high + low) / 2
print("Bisection Root:", ans)
print('Iterations:', iterations)

