#!/usr/bin/env python3
""" Boolinger """

import sys


def get_info(file):
    """ Récupérer le contenu d'un fichier """

    try:
        with open(file, "r") as file_fd:
            content = file_fd.read()
    except IOError:
        print("OMG LE FOCHIER")
        return 1
    print(content)


def main():
    """ Fonction main """

    get_info(sys.argv[1])
    return 1

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
