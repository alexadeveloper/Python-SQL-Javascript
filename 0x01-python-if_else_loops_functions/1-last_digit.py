#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    digit = (((number) * -1) % 10) * -1
else:
    digit = (number) % 10
inicio = "Last digit of"
if digit > 5:
    print("{} {} is {} and is greater than 5".format(inicio, number, last))
elif digit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, digit))
elif digit < 6:
    print("{} {} is {} and is less than 6 and not 0".format(number, digit))
