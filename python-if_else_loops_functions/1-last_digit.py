#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
_digit = abs(number) % 10
if number >= 0:
    _digit = int(repr(number)[-1])
else:
    _digit = int(repr(number)[-1]) * -1


if _digit > 5 and _digit != 0:
    print(f"Last digit of {number} is {_digit} and is greater than 5")
elif _digit == 0:
    print(f"Last digit of {number} is 0 and is 0")
elif _digit < 6 and _digit != 0:
    print(f"Last digit of {number} is {_digit} and is less than 6 and not 0")
