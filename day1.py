#!/usr/bin/env python3

with open('ex1_notes.txt', 'r') as file:
    open_file = file.readlines()
    total_number = [] 
    for i in open_file:
        number = []
        for j in i:
            if j.isdigit():
                number.append(j)
        total_number.append(int(number[0] + number[-1]))
    print(sum(total_number))
    
#        total_number.append(number[0] + number[-1])
#        for result in total_number:
#            print(result)
#