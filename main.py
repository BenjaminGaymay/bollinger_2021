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

def main():
    """ Fonction main """

    array = get_info(sys.argv[1])
    if array is None:
        print_help()
        return False
    return True

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
