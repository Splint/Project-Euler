#!/bin/env python

import math

TARGET_NUM = 1000

def isWhole(n):
    if n % 1 == 0:
        return True
    else:
        return False

def main():
    result = 0
    done = False
    print "Project Euler Problem #9"
    print "A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,\n"
    print "a^2 + b^2 = c^2\n"
    print "For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2\n"
    print "There exists exactly one Pythagorean triplet for which a + b + c = 1000."
    print "Find the product abc.\n"
    
    for a in range(1, 10000):
        if done:
            '''We need to break out of the nested for loop somehow'''
            break

        for b in range((a + 1), 10000):
            c_sqr = (a * a) + (b * b)
            c = math.sqrt(c_sqr)
            if isWhole(c) == True:
                if int(c) == (1000 - a - b):
                    result = a * b * int(c)
                    done = True
                    break

                else:
                    continue

            else: continue

    print "Final Answer: ", result

if __name__ == "__main__":
    main()
