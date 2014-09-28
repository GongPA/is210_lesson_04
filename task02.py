#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Task 02: Prompting inside a Loop Part I
"""

VALID = False
INPUT_NUM = 0
FACTORIAL = 1
PRODUCT = 1
# check input for number or non-number
while not VALID:
    INPUT_NUM = int(raw_input("Enter number >> "))
    if INPUT_NUM > 0:
        VALID = True
    else:
        print "Invalid number: Please enter a number greater than zero."
while FACTORIAL <= INPUT_NUM:
    PRODUCT *= FACTORIAL
    FACTORIAL += 1
print "Factorial of {} is {}".format(INPUT_NUM, PRODUCT)
