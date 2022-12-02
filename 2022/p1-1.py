#!/usr/bin/env python
# -*- coding: utf-8 -*-

filename = 'p1-input.txt'
#filename = 'p1-input-easy.txt'

def test():
    cals = []
    with open(filename, "r") as f:
        num = 0
        max_elf = 0
        elf = 0
        for row in f:
            if (row == "\n"):
                if (elf > max_elf): max_elf = elf
                elf = 0
                continue
            elf += int(row.strip())
            num += 1
            
        print (max_elf)

if __name__ == "__main__":
    test()
