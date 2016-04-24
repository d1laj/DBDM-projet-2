import numpy as np

def ans_to_char(i):
    if i == 0:
        return 'H'
    if i == 1:
        return 'D'
    if i == 2:
        return 'A'


def write_in_file(filename, ID, Answers):
    f = open(filename, 'w')
    f.write('ID,FTR\n')
    for i in range(len(ID)):
        f.write(str(ID[i]) + ',' + ans_to_char(Answers[i]) + '\n')
    f.close()
