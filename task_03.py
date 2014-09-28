#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Prompting inside a loop part 2"""

import data

ACCESS = False
NUM_GUESS = 3

while not ACCESS:
    PASSWORD = raw_input("What is your password ({0} attempts left)? "
                         "".format(NUM_GUESS))
    print PASSWORD
    if PASSWORD == data.PASSWORD:
        ACCESS = True
        print "Your Access is granted!"
        #giving a message for result.
    else:
        NUM_GUESS -= 1
        if NUM_GUESS == 0:
            print "Access denied. Please try again later."
            break
