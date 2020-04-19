# Finger exercise: What would the code in Figure 3.4 do if the 
# statement x = 25 were replaced by x = -25? 

# Finger exercise: 
# What would have to be changed to make the code in Figure 3.4 
# work for finding an approximation to the cube root of both 
# negative and positive numbers? (Hint: think about changing 
# low to ensure that the answer lies within the region being 
# searched.)

x = -8
epsilon = 0.01
numGuesses = 0
low = min(0, x)
high = max(1.0, x)
ans = (high + low) / 2
while abs(ans**3 - x) >= epsilon:
    print('low = ', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = ( high + low) / 2
print('numGuesses =', numGuesses)
print(ans, 'is close to square root of', x)