#!/usr/bin/env python3
""" Print help """
import sys


def print_help():
    """ Display help and exit """

    print("""Bollinger Bands

USAGE
    ./bollinger [-h] period standard_dev indexes_file index_number

    period          number of indexes for the moving average
    standard_dev    standard deviation coefficient to apply
    indexes_file    file containing daily indexes
    index_number    index number to compute moving average and Bollinger bands
    
OPTIONS
    -h              print the usage and quit.""", file=sys.stderr)
