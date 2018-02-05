#!/usr/bin/env python3
""" Boolinger """

import sys
from print_help import print_help


def split_file(file, period=True):
    """ Formater le fichier en tableau """

    array = file.split('\n')

    if period is True:
        return array[-PERIOD:]
    return array



def get_file(file):
    """ Récupérer le contenu d'un fichier """

    try:
        with open(file, "r") as file_fd:
            content = file_fd.read()
    except IOError:
        print("Error: File '%s' doesn't exist." % file)
        return None

    return content


def show_input():
    """ Afficher les inputs """

    print("Input:\nIndex: %d" % INDEX)
    print("Period: %d" % PERIOD)
    print("SD_coef: %.2f\n" % SD_COEF)


def main():
    """ Fonction main """

    content = get_file(sys.argv[1])
    if content is None:
        print_help()
        return False
    array = split_file(content)
    print(array)
    show_input()
    return True

if __name__ == "__main__":
    INDEX = 1
    PERIOD = 20
    SD_COEF = 1.5
    if len(sys.argv) is not 1:
        main()
