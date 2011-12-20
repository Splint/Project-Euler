#!/bin/env python
import math

def factors(n):
    factors = 0
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            factors += 2
    return factors

def get_answer():
    a = 0
    tri = 0
    while True:
        a += 1
        tri += a
        if factors(tri) > 500:
            return tri
            False
def main():
    print "Project Euler Problem #12"
    print "Final Answer: ", get_answer()

if __name__ == "__main__":
    main()
