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


def main():
    """ Fonction main """

    array = get_info(sys.argv[1])
    if array is None:
        return False
    return True

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
