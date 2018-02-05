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

def std_deviation(results):
    print(results.get_ma())