#!/bin/env python

alpha_array = { "A":1, "B":2, "C":3, "D":4,
                "E":5, "F":6, "G":7, "H":8,
                "I":9, "J":10, "K":11,"L":12,
                "M":13, "N":14, "O":15, "P":16,
                "Q":17, "R":18, "S":19, "T":20,
                "U":21, "V":22, "W":23, "X":24,
                "Y":25, "Z":26 }

def calc_names():
    result = 0
    count = 0
    file = open('names_mod.txt', 'r+')
    for name in file:
        name = name.rstrip('\n')
        count += 1
        for letter in name:
            result += alpha_array[letter] * count
    return result

def sort_file():
    file = open('names.txt', 'r+')
    file_new = open('names_mod.txt', 'w')
    line = file.readline().replace(",", "\n")
    line = sorted(line.split(), key=str.upper)
    for name in line:
        file_new.write("%s\n" % name.replace("\"", ""))
    file.close()
    file_new.close()

def main():
    print "Project Euler Problem #22"
    sort_file()
    print "Final Answer: ", calc_names()

if __name__ == "__main__":
    main()
