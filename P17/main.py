#!/bin/env python

TARGET = 1000

num_dic = { 1: 'one', 2: 'two', 3: 'three',
            4: 'four', 5: 'five', 6: 'six',
            7: 'seven', 8: 'eight', 9: 'nine',
            10: 'ten', 11: 'eleven', 12: 'twelve',
            13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
            16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
            19: 'nineteen', 20: 'twenty', 30: 'thirty',
            40: 'forty', 50: 'fifty', 60: 'sixty',
            70: 'seventy', 80: 'eighty', 90: 'ninety'}

def sum_double_digit(k, sum_one_to_nine):
    result = 0
    result += (len(num_dic[k]) * 9) + sum_one_to_nine
    return result

def calculate():
    result = 0
    sum_one_to_nine = 0
    hundred_and = 10
    thousand = 8
    global TARGET
   
    '''
    Determine the summation of 1 - 9
    so that it can be used faster
    '''
    for i in range(1, 10):
        sum_one_to_nine += len(num_dic[i])

    '''
    This is where we deal with 1 - 99
    '''
    for j in range(1, 21):
        if j <= 20:
            result += len(num_dic[j])

    for k in range(20, 100, 10):
        if k >= 30:
            result += len(num_dic[k])
        result += sum_double_digit(k, sum_one_to_nine)
    
    '''
    This is where we deal with over 100 - 999
    ''' 
    for l in range(1, 10):
        result += len(num_dic[l]) + 7
        for v in range(1, 21):
            if v <= 20:
                result += (len(num_dic[l]) + hundred_and) + len(num_dic[v])
        
        '''
        Since this function is iterating by 10, we need to
        multiple by 9 to the "one hundred and" part to 
        cover all the word count when we go from :
            21-30
            31-40
            51-60
            etc.
        '''
        for h in range(20, 100, 10):
            if h >= 30:
                result += len(num_dic[l]) + hundred_and + len(num_dic[h])
            result += (len(num_dic[l]) + hundred_and) * 9 + sum_double_digit(h, sum_one_to_nine)

    '''
    Count in 1000
    '''
    result += len(num_dic[1]) + thousand

    return result

def main():
    print "Project Euler Problem #17"
    print "Final Answer: ", calculate()

if __name__ == "__main__":
    main()
