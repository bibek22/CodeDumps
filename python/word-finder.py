#!/usr/bin/env python

common = input("What part gets changed ? : ")
common = common.lower()
english = open("/usr/share/dict/american-english", 'r')
spanish = open("/usr/share/dict/spanish", 'r')
count = 0

while count < 119520:
    count += 1
    word = english.readline().lower()
    new = ''
    if common in word:
        new = word.split(common)
        if new[1] == '\n':
            new = word.split(common)[0].lower()
            for line in spanish:
                if new in line:
                    print(line)
