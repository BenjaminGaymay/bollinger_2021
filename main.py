#!/usr/bin/env python3
""" Boolinger """

import sys
from help_file import print_help
from output_variables import OutputVariables
from calcul import std_deviation, moving_average, calcul_bands
#import matplotlib.pyplot as plt


def split_file(file, period=True):
    """ Formater le fichier en tableau """

    array = file.split('\n')

    array = [line.strip(' ') for line in array]
    array = list(filter(None, array))

    if period is True:
        return array[-PERIOD:]

    return array


def get_file(file):
    """ Récupérer le contenu d'un fichier """

    try:
        with open(file, "r") as file_fd:
            content = file_fd.read()
    except IOError:
        print("Error: File '%s' doesn't exist." % file, file=sys.stderr)
        return None

    return content


def show_input():
    """ Afficher les inputs """

    print("Input:\nIndex: %d" % INDEX)
    print("Period: %d" % PERIOD)
    print("SD_coef: %.2f\n" % SD_COEF)


def show_output(resuls):
    """ Afficher les inputs """

    print("Output:\nMA: %.2f" % resuls.get_ma())
    print("SD: %.2f" % resuls.get_sd())
    print("B+: %.2f" % resuls.get_plus())
    print("B-: %.2f" % resuls.get_minus())


def fill_results(array, results):
    """ Récupérer les valeurs calculées """

    results.set_ma(moving_average(array))
    results.set_sd(std_deviation(results, array))
    results.set_plus(calcul_bands(results, SD_COEF))
    results.set_minus(calcul_bands(results, SD_COEF, False))


def main():
    """ Fonction main """

    content = get_file(sys.argv[1])
    if content is None:
        return False
    array = split_file(content)

    results = OutputVariables()

    fill_results(array, results)
    show_input()
    show_output(results)
    return True


if __name__ == "__main__":

    # INPUTS VARIABLES
    INDEX = 1
    PERIOD = 20
    SD_COEF = 2

    if len(sys.argv) is not 1:
        main()
    else:
        print_help()
