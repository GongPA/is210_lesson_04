#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Task 04:
Looping Mathematical Calculations
"""

import data

TOTAL = 0
MINIMUM = 0
MAXIMUM = 0

for DAY in data.TRANSACTIONS:
    DAY_TOTAL = 0
    for SINGEL_TRANS in DAY:
        DAY_TOTAL += int(SINGEL_TRANS)
    TOTAL += DAY_TOTAL
    if DAY_TOTAL < MINIMUM:
        MINIMUM = DAY_TOTAL
    if DAY_TOTAL > MAXIMUM:
        MAXIMUM = DAY_TOTAL
