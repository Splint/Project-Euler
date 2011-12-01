#!/bin/env python

MAX_NUM = 999
MIN_NUM = 100

def isPalindrome(n):
    n_str = str(n)
    if n_str == n_str[::-1]:
        return True
    else:
        return False

def main():
    largest_pal_num = 0
    answer = 0
    print "Project Euler Problem #4"
    print "A palindromic number reads the same both ways. The largest palindrome made from"
    print "the product of two 2-digit numbers is 9009 = 91 x 99."
    print
    print "Find the largest palindrome made from the product of two 3 digit numbers."
    print
    for first_num in range(MAX_NUM, MIN_NUM, -1):
        for second_num in range(MAX_NUM, MIN_NUM, -1):
            answer = first_num * second_num
            if isPalindrome(answer) == True:
                if largest_pal_num < answer:
                    largest_pal_num = answer
                else:
                    continue
            else:
                continue

    print "Final Answer: ", largest_pal_num

main()

