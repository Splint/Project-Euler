#!/bin/env python

MIN_NUM = 1
MAX_NUM = 20

def main():
    print "Project Euler Problem #5"
    print "2520 is the smallest number that can be divided by each of the numbers from"
    print "1 to 10 without any remainder."
    print
    print "What is the smallest positive number that is evenly divisible by all the"
    print "numbers from 1 to 20?"
    print
    
    i = 1
    for k in range(MIN_NUM, (MAX_NUM + 1)):
        if i % k > 0:
            for j in range(MIN_NUM, (MAX_NUM + 1)):
                if (i * j) % k == 0:
                    i *= j
                    break

    print "Final Answer: ", i
    
if __name__ == "__main__":
    main()
