#!/usr/bin/python3
"""
Accept 2 values from user and store in variables num1 and num2.
Convert the values (str) to numbers (int).
Perform calculations on the values: add, subtract, multiply, divide, modulus.
Print the result.
"""


#  Accept 2 values from user and store in variables num1 and num2
num1, num2 = input("Enter 2 values: ").split()
num1 = int(num1)
num2 = int(num2)

#  Perform calculations on the values: add, subtract, multiply, divide, modulus
sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
mod = num1 % num2

#  Print the result
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, sub))
print("{} * {} = {}".format(num1, num2, mul))
print("{} / {} = {}".format(num1, num2, div))
print("{} % {} = {}".format(num1, num2, mod))
