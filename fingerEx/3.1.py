# Finger exercise: Write a program that asks the user to enter an 
# integer and prints two integers, root and pwr, such 
# that 0 < pwr < 6 and root**pwr is equal to the integer entered 
# by the user. If no such pair of integers exists, it should 
# print a message to that effect.

x = int(input("Enter an integer:"))

ans = False

for root in range(x - 1, 0, -1):
    for pwr in range(1, 7):
        if int(root) ** int(pwr) == x:
            print("root", root, "pwr", pwr)
            ans = True
            break

if ans == False:
    print("Nah fam...")


root = x - 1
while root > 0:
    pwr = 1
    while pwr < 6:
        if root ** pwr == x:
            print("root", root, "pwr", pwr)
            ans = True
            break
        pwr = pwr + 1
    root = root - 1

if ans == False:
    print("Nah fam...")
    