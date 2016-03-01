#!/usr/bin/python

import time
import primeMod as pm
start = time.time()


def fifth_power(n=0):
    # returns dictionary of fifth_power of digits.
    result = []
    if n == 0:
        for each in range(10):
            result.append(each**5)
        return result
    else:
        return n**5


power = fifth_power()
for each in power:
    
