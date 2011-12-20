#!/bin/env python

TARGET_NUM = 600851475143

def isPrime(n):
    '''Determine if the number `n` is prime'''
    for num in range(2, int(n**0.5)+1):
        if n % num == 0:
            return False
    return True

def main():
    largest_prime_num = 0
   
    print "Project Euler Problem #3"
    for num in range(1, int(TARGET_NUM**0.5)+1):
        if TARGET_NUM % num == 0:
            if (isPrime(num) == True):
                if(largest_prime_num < num):
                    largest_prime_num = num
                else:
                    continue
            else:
                continue
        else:
            continue

    print "Final Answer: ", largest_prime_num

main()

