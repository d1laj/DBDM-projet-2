import numpy as np

def ans_to_char(i):
    if i == -1:
        return 'H'
    if i == 0:
        return 'D'
    if i == 1:
        return 'A'


def write_in_file(filename, ID, Answers):
    f = open(filename, 'w')
    f.write('ID,FTR\n')
    for i in range(ID.size):
        f.write(str(ID[i]) + ',' + ans_to_char(Answers[i]) + '\n')
    f.close()
