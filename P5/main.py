#!/bin/env python

MIN_NUM = 1
MAX_NUM = 20

def main():
    print "Project Euler Problem #5"
    i = 1
    for k in range(MIN_NUM, (MAX_NUM + 1)):
        if i % k > 0:
            for j in range(MIN_NUM, (MAX_NUM + 1)):
                if (i * j) % k == 0:
                    i *= j
                    break

    print "Final Answer: ", i
    
if __name__ == "__main__":
    main()
