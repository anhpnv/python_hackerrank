#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    logo_character = list(set(s))
    count = 0
    character = dict()
    for y in logo_character:
        for i in s:
            if y == i:
                count += 1
        if count in character.keys():
            character[count] = sorted(list((*character[count], y)))
        else:
            character[count] = [y]
        count = 0
    keylist = sorted(character.keys(), reverse=True)
    if len(character[keylist[0]]) >= 3:
        print(character[keylist[0]][0], keylist[0])
        print(character[keylist[0]][1], keylist[0])
        print(character[keylist[0]][2], keylist[0])

    elif len(character[keylist[0]]) == 2:
        print(character[keylist[0]][0], keylist[0])
        print(character[keylist[0]][1], keylist[0])
        print(character[keylist[1]][0], keylist[1])

    elif len(character[keylist[0]]) == 1:
        print(character[keylist[0]][0], keylist[0])
        print(character[keylist[1]][0], keylist[1])
        if len(character[keylist[1]]) >= 2:
            print(character[keylist[1]][1], keylist[1])
        else:
            print(character[keylist[2]][0], keylist[2])
        
        
