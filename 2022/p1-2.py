#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sortedcontainers import SortedList

filename = 'p1-input.txt'
#filename = 'p1-input-easy.txt'

def test():
    cals = []
    with open(filename, "r") as f:
        num = 0
        elves = SortedList()
        elves.add(0)
        elves.add(1)
        elves.add(5)
        
        elf = 0
        for row in f:
            if (row == "\n"):
                print ("elf: " + str(elf))
                print (elves)

                if (elf > elves[0]):
                    del elves[0]
                    elves.add(elf)
                    
                    
                
                elf = 0
                continue
            elf += int(row.strip())
            num += 1

        
        tot_elf = 0
        print ("final: ")
        print (elves)
        for e in elves:
            tot_elf += e
        print (tot_elf)

if __name__ == "__main__":
    test()
