"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
aside= float(input("Give me a number"))
bside= float(input("Give me another number"))
list = [aside,bside]
list.sort()
min = list[0]
bigg = list[1] 

cside= str(input("Is one of those the hypotenuse? Yes or No"))
if cside == "Yes":
    cside= (bigg**2 - min**2)**0.5
    cside = round(cside,1)
    print (f'{cside} is the missing side')
else:
    cside= (min**2 + bigg**2)**0.5
    cside = round(cside,1)
    print(f'{cside} is the hypotenuse')