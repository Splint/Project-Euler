#!/bin/env python

TARGET_NUM = 100

def main():
    sum_of_squares = 0
    square_of_sums = 0
    diff = 0

    print "Project Euler Problem #6"
    for num in range(1, (TARGET_NUM + 1)):
        sum_of_squares += num * num
        square_of_sums += num
    
    square_of_sums = square_of_sums * square_of_sums
        
    diff = square_of_sums - sum_of_squares

    print "Final Answer: ", diff
        
if __name__ == "__main__":
    main()
