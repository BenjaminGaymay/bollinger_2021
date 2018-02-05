#!/usr/bin/env python3
""" Does moving average """


def moving_average(array):
    """ Does moving average """

    avg = 0
    len_arr = len(array)
    for x in range(0, len_arr):
        avg += float(array[x])
    avg /= len_arr
    avg = round(avg, 2)
    return avg

def std_deviation(results, array):
    res = 0
    for x in range(0, len(array)):
        res += pow(abs(float(array[x]) - results.get_ma()), 2)
    res /= len(array)
    res = pow(res, 0.5)
    return res

def calcul_bands(results, sd_coef, operation=True):
    if (operation is True):
        return results.get_ma() + (results.get_sd() * sd_coef)
    else:
        return results.get_ma() - (results.get_sd() * sd_coef)