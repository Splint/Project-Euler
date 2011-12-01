#!/bin/env python

MIN_NUM = 1
MAX_NUM = 20

def main():
    smallest_num = 0
    print "Project Euler Problem #5"
    print "2520 is the smallest number that can be divided by each of the numbers from"
    print "1 to 10 without any remainder."
    print
    print "What is the smallest positive number that is evenly divisible by all the"
    print "numbers from 1 to 20?"
    print
    
    counter = 0
    while(smallest_num == 0):
        counter += 1
        print counter
        for num in range(MIN_NUM, (MAX_NUM+1)):
            if counter % num == 0:
                if num == MAX_NUM:
                    smallest_num = counter
                    break
            else:
                break

    print "Final Answer: ", smallest_num
main()
