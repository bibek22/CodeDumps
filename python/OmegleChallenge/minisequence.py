#!/usr/bin/python

mainSquence = []
correctSequence = []
# to keep track of previous match of required condition
# in the loop immediately below
streak = 0
longest = 1
for index in range(2, len(mainSquence)-2):
    if mainSquence[index] == mainSquence[index - 1] + mainSquence[index - 2]:
        correctSequence.append(index-2)
        correctSequence.append(3)
        if streak == 1:
            correctSequence[-1] += 1

for i in range(1, len(correctSequence), 2):
    if correctSequence[i] > correctSequence[longest]:
        longest = i


def rightcheck(index):
