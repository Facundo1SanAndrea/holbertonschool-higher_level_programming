#!/usr/bin/python3
for number in range (0, 9):
  if number == 8:
    print(89)
  else:
    for x in range (number + 1, 10):
      print("{}{} ,".format(number, x), end="")