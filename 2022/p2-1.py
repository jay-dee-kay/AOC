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

        #  A    X    ROCK
        #  B    Y    PAPER
        #  C    Z    SCISSORS
        
        if t == 'A':
            if m == 'X': score += 3
            if m == 'Y': score += 6
        if t == 'B':
            if m == 'Y': score += 3
            if m == 'Z': score += 6
        if t == 'C':
            if m == 'Z': score += 3 
            if m == 'X': score += 6

        if m == 'X': score += 1 
        if m == 'Y': score += 2
        if m == 'Z': score += 3

        print (t + " vs. " + m + " == score of " + str(score))
        total += score

    print ("")
    print ("Final Total: " + str(total))
        

if __name__ == "__main__":
    test()
