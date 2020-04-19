# Finger exercise: Let s be a string that contains a
# sequence of decimal numbers separated by commas,
# e.g., s = '1.23,2.4,3.123'. Write a program that
# prints the sum of the numbers in s.

s = '1.23,2.4,3.123'

num = ''
total = 0

for c in s:
    if (c != ','):
        num = num + c
    else:
        total = total + float(num)
        num = ''
total = total + float(num)

print('total:', total)
