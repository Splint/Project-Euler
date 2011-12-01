#!/bin/env python

TARGET_NUM = 10001
MAX_NUM = 1000000
MIN_NUM = 2

def isPrime(n):
    for num in range(2, int(n**0.5)+1):
        if n % num == 0:
            return False
    return True

def main():
    target_prime = 0
    count = 0
    print "Project Euler Problem #7"
    print "By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see"
    print "that the 6th prime is 13.\n"
    print "What is the 10 001st prime number?\n"
    for num in range(MIN_NUM, MAX_NUM):
        if isPrime(num) == True:
            count += 1
            if count == TARGET_NUM:
                target_prime = num
                break

    print "Final Answer: ", target_prime

if __name__ == "__main__":
    main()
