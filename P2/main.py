#!/bin/env python

MAX_NUM = 35
MIN_NUM = 1

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def main():
    temp_fib = 0;
    answer = 0;
    
    print "Project Euler Problem #2"
    for num in range(MIN_NUM, MAX_NUM):
        temp_fib = fib(num)
        if temp_fib < 4000000:
            if temp_fib % 2 == 0:
                answer += temp_fib

    print "Final Answer: ", answer

main()
