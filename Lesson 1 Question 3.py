string1 = input("Please enter any string: ")

num1 = 0
space1 = 0

for i in string1:
    if (i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9'):
        num1 = num1 + 1
    if (i == ' '):
        space1 = space1 + 1

print("The number of numbers in the string is: ")
print (num1)

print("The number of letters in the string is: ")
print (len(string1) - num1 - space1)

print("The number of words in the string is: ")
print(space1 + 1)