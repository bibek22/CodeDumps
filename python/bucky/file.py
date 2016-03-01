#!/usr/bin/python

fw = open("new.txt", 'w')
fw.write("writing things into a file.\n")
fw.write("I don't like bacon.\n")
fw.close

fr = open("new.txt", 'r')
text = fr.read()
print(text)
fr.close()
