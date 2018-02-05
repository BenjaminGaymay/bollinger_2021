#!/usr/bin/env python3
""" Output Variables """


class OutputVariables:
    """ Variables output """
    def __init__(self):
        """ Initialisation des variables """
        self._ma = 0
        self._sd = 0
        self._plus = 0
        self._minus = 0

    def set_ma(self, new_ma):
        """ Setter _ma """
        self._ma = new_ma

    def get_ma(self):
        """ Getter _ma """
        return self._ma

    def set_sd(self, new_sd):
        """ Setter _sd """
        self._sd = new_sd

    def get_sd(self):
        """ Getter _sd """
        return self._sd

    def set_plus(self, new_plus):
        """ Setter _plus """
        self._plus = new_plus

    def get_plus(self):
        """ Getter _plus """
        return self._plus

    def set_minus(self, new_minus):
        """ Setter _minus """
        self._minus = new_minus

    def get_minus(self):
        """ Getter _minus """
        return self._minus
