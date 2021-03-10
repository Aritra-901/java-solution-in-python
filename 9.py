#Two numbers are entered through the keyboard. Write a program to find the value of one number raised to the power of another.

import math

number = int(input(" Please Enter any Positive Integer : "))
exponent = int(input(" Please Enter Exponent Value : "))

power = math.pow(number, exponent)

print("The Result of {0} Power {1} = {2}".format(number, exponent, power))