#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 1: Analyze a string
    (1)Split into lines
    (2)Split into works
    (3)Using a nested loop
"""

import data
print data.SHAKESPEARE
MAXIMUM_WORDS = 0
MINIMUM_WORDS = 100
AVERAGE_WORDS = 0
CRISPIAN = 0
TOTAL_WORDS = 0
LINES = data.SHAKESPEARE.split('\n') 
for LINE in LINES:
    WORDS = LINE.split()
    WORDSIZE = len(WORDS)
    TOTAL_WORDS += WORDSIZE
    if WORDSIZE > MAXIMUM_WORDS:
        MAXIMUM_WORDS = WORDSIZE
    if WORDSIZE < MAXIMUM_WORDS:
        MINIMUM_WORDS = WORDSIZE
    if "Crispian" in LINE:
        CRISPIAN += 1
AVERAGE_WORDS = float(TOTAL_WORDS)/float(len(LINES))
print MAXIMUM_WORDS, MINIMUM_WORDS, TOTAL_WORDS, AVERAGE_WORDS, CRISPIAN
