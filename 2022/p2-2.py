#!/usr/bin/env python
# -*- coding: utf-8 -*-

filename = 'p2-input.txt'
#filename = 'p2-input-easy.txt'

def test():
    them  = []
    me    = []
    
    with open(filename, "r") as f:
        for row in f:
            (t,m) = row.strip().split(" ")
            them.append(t)
            me.append(m)
            
        
    round = 0
    total = 0
    
    for t in them:
        m = me[round]
        
        score = 0
        round += 1
        print (str(round) + ": " + t + " vs. " + m + " == score of " + str(score))

        #  A    X    ROCK       LOSE
        #  B    Y    PAPER      TIE
        #  C    Z    SCISSORS   WIN
        
        if m == 'X': score += 0 
        if m == 'Y': score += 3
        if m == 'Z': score += 6

        if t == 'A':
            if   m == 'X': m = "Z"
            elif m == 'Y': m = "X"
            elif m == 'Z': m = "Y"
            
        if t == 'B':
            if   m == 'X': m = "X"
            elif m == 'Y': m = "Y"
            elif m == 'Z': m = "Z"
            
        if t == 'C':
            if   m == 'X': m = "Y"
            elif m == 'Y': m = "Z"
            elif m == 'Z': m = "X"

        if m == 'X': score += 1 
        if m == 'Y': score += 2
        if m == 'Z': score += 3

        print (t + " vs. " + m + " == score of " + str(score))
        total += score

    print ("")
    print ("Final Total: " + str(total))
        

if __name__ == "__main__":
    test()
