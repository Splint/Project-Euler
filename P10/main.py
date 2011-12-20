#!/bin/env python

MAX_NUM = 2000000
MIN_NUM = 2

def isPrime(n):
    for num in range(2, int(n**0.5)+1):
        if n % num == 0:
            return False
    return True

def main():
    sum_primes = 0
    prime_list = []

    print "Project Euler Problem #10"
    for num in range(MIN_NUM, MAX_NUM):
        if isPrime(num) == True:
            prime_list.append(num)

    sum_primes = sum(prime_list)

    print "Final Answer: ", sum_primes

if __name__ == "__main__":
    main()
