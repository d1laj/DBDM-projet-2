import numpy as np


def read_train(train):
    a = False
    f = open(train, 'r+')
    ID = []
    data = []
    answers = []
    date = []
    for line in f:
        if not a:
            a = True
            continue

        line_list = line.split(',')
        line_list[1] = line_list[1].replace("-", "")

        ID.append([int(line_list[0]), line_list[2], line_list[3]])

        del line_list[0]
        del line_list[1]
        del line_list[1]

        if (line_list[1] == "A"):
            line_list[1] = "1"
        if (line_list[1] == "D"):
            line_list[1] = "0"
        if (line_list[1] == "H"):
            line_list[1] = "-1"
        if (line_list[-1][-1] == '\n'):
            line_list[-1] = line_list[-1][:-1]

        for i in range(len(line_list)):
            if (line_list[i] == "NA"):
                line_list[i] = np.nan
            line_list[i] = float(line_list[i])

        date.append(line_list[0])
        del line_list[0]
        answers.append(line_list[0])
        del line_list[0]
        data.append(line_list)
    return ID, data, answers, date

# ID, data = read_train('train.csv')
# print(data)