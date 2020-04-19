# Finger exercise: Write a program that asks the user to input 10
# integers, and then prints the largest odd number that was entered.
# If no odd number was entered, it should print a message to that effect.

length = 10

integers = []

i = 0
while i < length:
    integers.append(int(input("Enter number [" + str(i) + "]: ")))
    i = i + 1

greatest = False
j = 0
while j < length:
    if (integers[j] % 2 == 1):
        greatest = greatest if greatest > integers[j] else integers[j]
    j = j + 1

if greatest:
    print("Greatest odd number:", greatest)
else:
    print("No odd numbers")
