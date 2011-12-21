#!/bin/env python

TARGET = 1000

def summation(n):
    offset = 1
    result = 0
    n_str = str(n)
    LEN = len(n_str)
    for i in range(0, LEN):
        result += int(n_str[i:offset])
        offset += 1
    return result

def calc_exp():
    global TARGET
    result = 1
    for i in range (0, TARGET):
        result *= 2
    return result

def main():
    print "Project Euler Problem #16"
    print "Final Answer: ", summation(calc_exp())

if __name__ == "__main__":
    main()
