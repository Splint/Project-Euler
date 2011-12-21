#!/bin/env python

import math

TARGET = 100

def calculate():
    global TARGET
    result = 0
    offset = 1
    fac = 0
    fac = math.factorial(TARGET)
    fac_str = str(fac).rstrip('\n')
    for i in range(0, len(fac_str)):
        result += int(fac_str[i:offset])
        offset += 1
    return result

def main():
    print "Project Euler Problem #20"
    print "Final Answer: ", calculate()

if __name__ == "__main__":
    main()
