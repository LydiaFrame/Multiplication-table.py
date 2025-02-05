#!/usr/bin/env python3

"""Write a program to print a multiplication table"""

__author__="Lydia Frame"
__date__="02/05/2025"

#Prompt user for starting num of multiplication table
while True:
    start = int(input("Start? "))
    print()
    if 1<=start<=10:
        break

#Prompt user for ending num of multiplication table
while True:
    stop = int(input("Stop? "))
    print()
    if 1 <= stop <= 10 and stop >= start:
        stop+=1
        break

print("*", end=" ")
for i in range(start, stop):
    print("(" + str(i) + ")", end="")
print()

for i in range(start, stop):
    print("(" + str(i) + ")", end=" ")
    for j in range(start, stop):
        multiply = i*j
        print(str(multiply), end=" ")
    print()

