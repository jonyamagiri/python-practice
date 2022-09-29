#!/usr/bin/python3
"""
Receives miles and convert to kilometers.
Kilometers = miles * 1.60934
Output: 5 miles equals 8.04 kilometers.
"""


miles = eval(input("Enter distance in miles: "))
kilometers = miles * 1.60934
print("{} miles equals {:.02f} kilometers.".format(miles, kilometers))
