#!/bin/env python

TARGET = 1000000
COMPARE_CNT = 0
COMPARE_CNT_NUM = 0

def compare(j, count):
    global COMPARE_CNT, COMPARE_CNT_NUM
    if COMPARE_CNT < count:
        COMPARE_CNT = count
        COMPARE_CNT_NUM = j

    return COMPARE_CNT_NUM

def calculate(i, j, count):
    if i == 1:
        compare(j, count)
        return

    if i % 2 == 0:
        i = i/2
        count += 1

    else:
       i = ((3 * i) + 1)
       count += 1

    calculate(i, j, count)

def loop_through():
    for i in range(2, TARGET):
        count = 0
        calculate(i, i, count)

def main():
    print "Problem Euler Problem #14"
    loop_through()
    print "Final Answer: ", COMPARE_CNT_NUM

if __name__ == "__main__":
    main()
