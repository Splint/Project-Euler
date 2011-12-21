#!/bin/env python

TARGET = 1000000

def seq(i):
    cnt = 1
    num_arr = [i]
    while i != 1:
        if i % 2 == 0:
            i = i / 2
        else:
            i = (3 * i) + 1
        cnt += 1
        num_arr += [i]
    return cnt

def main():
    global TARGET
    print "Project Euler Problem #14"
    f = {}
    for i in range(2, TARGET):
        x = seq(i)
        f[x] = i
    max_num = max(f)
    result = f[max_num]
    print "Final Answer: ", result

if __name__ == "__main__":
    main()
