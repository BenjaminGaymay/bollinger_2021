#!/usr/bin/env python3
""" Output Variables """


class OutputVariables:
    """ Variables output """
    def __init__(self):
        """ Initialisation des variables """
        self._ma = 0
        self._sd = 0
        self._b_plus = 0
        self._b_minus = 0

    def set_ma(self, new_ma):
        """ Setter _ma """
        self._ma = new_ma

    def get_ma(self):
        """ Getter _ma """
        return self._ma
