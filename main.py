#!/usr/bin/env python3
""" Boolinger """

import sys


def get_info(file):
    """ Récupérer le contenu d'un fichier """

    try:
        with open(file, "r") as file_fd:
            content = file_fd.read()
    except IOError:
        print("Wrong file")
        return None
    array = content.split("\n")
    return array


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


def show_input():
    """ Afficher les inputs """

    print("Input:\nIndex: %d" % INDEX)
    print("Period: %d" % PERIOD)
    print("SD_coef: %.2f\n" % SD_COEF)


def main():
    """ Fonction main """

    array = get_info(sys.argv[1])
    if array is None:
        print_help()
        return False

    show_input()
#    print(array[-PERIOD:])
    return True

if __name__ == "__main__":
    INDEX = 1
    PERIOD = 20
    SD_COEF = 1.5
    if len(sys.argv) is not 1:
        main()
