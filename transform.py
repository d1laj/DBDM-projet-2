import numpy as np
import math


def transform_data(X):
    """X est de la forme B365H, B365D, B365A, BWH, BWD, BWA, IWH, IWD, IWA, LBH, LBD, LBA, VCH, VCD, VCA, WHH, WHD, WHA"""
    for line in range(X.shape[0]):
        for i in range(6):
            H = X[line, i * 3]
            D = X[line, i * 3 + 1]
            A = X[line, i * 3 + 2]
            ratio_HD = H / D
            ratio_AD = A / D
            ratio_HA = H / A
            X[line, i * 3] = ratio_HD
            X[line, i * 3 + 1] = ratio_AD
            X[line, i * 3 + 2] = ratio_HA
    return X


def remove_nan(X):
    """X est de la forme B365H, B365D, B365A, BWH, BWD, BWA, IWH, IWD, IWA, LBH, LBD, LBA, VCH, VCD, VCA, WHH, WHD, WHA"""
    for line in range(X.shape[0]):
        ch = 0
        cd = 0
        ca = 0
        mean_h = 0
        mean_a = 0
        mean_d = 0
        for i in range(6):
            H = X[line, i * 3]
            D = X[line, i * 3 + 1]
            A = X[line, i * 3 + 2]  # Changer 2 par 1 nous fait gagner un peu ici
            if not math.isnan(H):
                mean_h += H
                ch += 1
            if not math.isnan(D):
                mean_d += D
                cd += 1
            if not math.isnan(A):
                mean_a += A
                ca += 1
        if ch == 0:
            mean_h = 1.0
        else:
            mean_h = mean_h / ch
        if cd == 0:
            mean_d = 1.0
        else:
            mean_d = mean_d / cd
        if ca == 0:
            mean_a = 1.0
        else:
            mean_a = mean_a / ca
        for i in range(6):
            H = X[line, i * 3]
            D = X[line, i * 3 + 1]
            A = X[line, i * 3 + 2]  # Changer 2 par 1 nous fait gagner un peu ici
            if math.isnan(H):
                H = mean_h
            if math.isnan(D):
                D = mean_d
            if math.isnan(A):
                A = mean_a
            X[line, i * 3] = H
            X[line, i * 3 + 1] = D
            X[line, i * 3 + 2] = A
    return X


def transform_date(date):
    week = {}
    for i in date:
        week[i] = True
    count = 1
    for key in sorted(week.keys()):
        week[key] = count
        count += 1
    for i in range(len(date)):
        date[i] = week[date[i]]
    return date
