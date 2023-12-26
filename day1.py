#!/usr/bin/env python3

with open('ex_notes.txt', 'r') as file:
    opened_file = file.readlines()
    sum_nubmer1 = 0
    sum_nubmer2 = 0
    num = ["zero","one","two","three","four","five","six","seven","eight","nine"]

    def change(i):
        for n,nn in enumerate(num):
            i = i.replace(nn, f"{nn}{n}{nn}")
            #print(n,nn)
            
        return i

    for i in opened_file:
        total_number = [j for j in i if j.isnumeric()]
        #print(total_number)
        sum_nubmer1 += int(total_number[0] + total_number[-1])
    
    for i in opened_file:
        total_number = [j for j in change(i) if j.isnumeric()]
        #print(total_number)
        sum_nubmer2 += int(total_number[0] + total_number[-1])


    print(sum_nubmer1, sum_nubmer2)


another_example = """
digits_num = ["zero","one","two","three","four","five","six","seven","eight","nine"]
def tmp(path=None):
    path = open(f'{path}','r').readlines()
    sum_nubmer = 0
    for line in path: 
        total_number = [j for j in change(line) if j.isnumeric()]
        sum_nubmer += int(total_number[0] + total_number[-1])
    return sum_nubmer 


def change(line):
    for num,name in enumerate(digits_num):
        line = line.replace(name, f"{name}{num}{name}")
    return line 

path = 'ex_notes.txt'
tmp(path)
"""