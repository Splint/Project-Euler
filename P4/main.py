#!/bin/env python

#MAX_NUM = 999
#MIN_NUM = 100
MAX_NUM = 99
MIN_NUM = 10
def main():
    largest_pal_num = 0
    answer = 0
    print "Project Euler Problem #4"
    print "A palindromic number reads the same both ways. The largest palindrome made from"
    print "the product of two 2-digit numbers is 9009 = 91 x 99."
    print
    print "Find the largest palindrome made from the product of two 3 digit numbers."
    print
    for num in range(MIN_NUM, MAX_NUM):
        answer = MIN_NUM * num
        print MIN_NUM, "*", num, "=", answer
main()
