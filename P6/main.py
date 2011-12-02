#!/bin/env python

TARGET_NUM = 100

def main():
    sum_of_squares = 0
    square_of_sums = 0
    diff = 0
    print "Project Euler Problem #6"
    print "The sum of the squares of the first ten natural numbers is,\n"
    print "1^2 + 2^2 + ... + 10^2 = 385\n"
    print "The square of the sum of the first ten natural numbers is,\n"
    print "(1 + 2 + ... + 10)^2 = 55^2 = 3025\n"
    print "Hence the difference between the sum of the squares of the first ten"
    print "natural numbers and the square of the sum is 3025 - 385 = 2640\n"
    print "Find the difference between the sum of the squares of the first one"
    print "hundred natural numbers and the square of the sum.\n"

    for num in range(1, (TARGET_NUM+1)):
        sum_of_squares += num * num
        square_of_sums += num
    
    square_of_sums = square_of_sums * square_of_sums
        
    diff = square_of_sums - sum_of_squares

    print "Final Answer: ", diff
        
if __name__ == "__main__":
    main()
