# Finger exercise: Write a function isIn that accepts 
# two strings as arguments and returns True if either 
# string occurs anywhere in the other, and False otherwise. 
# Hint: you might want to use the built-in str operation in.

def isIn(stringOne, stringTwo):
    if stringOne in stringTwo or stringTwo in stringOne:
        return True
    
    return False

string1 = input("Enter a string:")
string2 = input("Enter another string:")

print("isIn", isIn(string1, string2));
