#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"

A = ' '.join(str.split()[5:7]) + " " + ''.join(str.split()[-4]) + " " + ' '.join(str.split()[:1])

print(A)
#print(B)
#print(C)
