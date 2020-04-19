# Finger exercise: Write a program that examines three variables—x, y,
# and z—and prints the largest odd number among them. If none of them
# are odd, it should print a message to that effect.

input_x = input("Enter number for x: ")
x = float(input_x)

input_y = input("Enter number for y: ")
y = float(input_y)

input_z = input("Enter number for z: ")
z = float(input_z)

# if x is odd
if (x % 2 == 1):
    # if y is odd
    if (y % 2 == 1):
        # if z is odd
        if (z % 2 == 1):
            # compare all three
            greatest = x if x > y and x > z else y if y > z else z
            print('greatest odd number:', greatest)
        else:
            # compare x and y
            greatest = x if x > y else y
            print('greatest odd number:', greatest)
    elif (z % 2 == 1):
        # compare x and z
        greatest = x if x > z else z
        print('greatest odd number:', greatest)
elif (y % 2 == 1):
    if (z % 2 == 1):
        greatest = y if y > z else z
        print('greatest odd number:', greatest)
    else:
        greatest = y
        print('greatest odd number:', greatest)
elif (z % 2 == 1):
    greatest = z
    print('greatest odd number:', greatest)
else:
    print('No odd numbers')
