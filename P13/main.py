#!/bin/env python

def calculate():
    answer = 0
    file = open('num.txt', 'r+')
    line = file.readline()

    while line:
        line = line.rstrip('\n')
        answer += long(line)
        line = file.readline()
    
    return answer

def main():
    print "Project Euler Problem 13"
    print "Final Answer: ", str(calculate())[0:10]


if __name__ == "__main__":
    main()
