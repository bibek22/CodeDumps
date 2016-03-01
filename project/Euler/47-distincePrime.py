#!/usr/bin/python

import primeMod as pm

length = 4
running_sum = 0
first = 0
start = 1
print(len(pm.factors(3)))

while running_sum != length:
    start += 1
    if len(pm.factors(start)) >= length:
        first = start
        running_sum += 1
        print(start)
    else:
        running_sum = 0

print(first-length+1)
