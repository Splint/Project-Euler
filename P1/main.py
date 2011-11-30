#!/bin/env python

MAX_NUM=1000
MIN_NUM=1
MULT_NUM_3=3
MULT_NUM_5=5

def main():
    answer = 0
    print "Project Euler ID #1"
    print "Add all the natural numbers below one thousand that are multiples of 3 or 5"
    print
    for num in range(MIN_NUM, MAX_NUM):
        if (num%3 == 0) | (num%5 == 0):
            answer += num
    
    print "Final Answer: ", answer

main()


