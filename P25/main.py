#!/bin/env python

TARGET = 1000
RANGE_NUM = 10000

def fib_gen():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

def run_fib():
    a = fib_gen()
    d = True
    term = 0
    a.next()
    for i in range(RANGE_NUM):
        if d == False:
            break
        term += 1
        fib_number = str(a.next())
        if len(fib_number) >= TARGET:
            d = False
    return term

def main():
    print "Project Euler Problem #25"
    print "Final Answer: ", run_fib()

if __name__ == "__main__":
    main()
