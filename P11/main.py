#!/bin/env/python

def main():
    print "Project Euler Problem #11"
    f = open('20x20.txt', 'rU')
    x = []
    max_prod = 0

    # Create list of lists with x
    for m in xrange(20):
        x.append([])
        for n in xrange(20):
            x[m].append(int(f.read(3)))
    
    f.close()


    # Check Horizontally for max_prod
    for i in range(len(x)):
        for j in range(len(x[i])-3):
            hori = (x[i][j])*(x[i][j+1])*(x[i][j+2])*(x[i][j+3])
            if hori > max_prod:
                max_prod = hori

    # Check Vertically for max_prod
    for i in range(len(x[i])-3):
        for j in range(len(x)):
            vert = (x[i][j])*(x[i+1][j])*(x[i+3][j])
            if vert > max_prod:
                max_prod = vert

    # Check diagonally right for max_prod
    for i in range(len(x[i])-3):
        for j in range(len(x[i])-3):
            diag_right = (x[i][j])*(x[i+1][j+1])*(x[i+2][j+2])*(x[i+3][j+3])
            if diag_right > max_prod:
                max_prod = diag_right

    # Check diagonally left for max_prod
    for i in range(3, len(x)):
        for j in range(len(x[i])-3):
            diag_left = (x[i][j])*(x[i-1][j+1])*(x[i-2][j+2])*(x[i-3][j+3])
            if diag_left > max_prod:
                max_prod = diag_left

    print "Final Answer: %s" % max_prod

if __name__ == "__main__":
    main()
