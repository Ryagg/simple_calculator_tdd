# -*- coding: utf-8 -*-

from functools import reduce


class SimpleCalculator:
    def add(self, *args):
        return sum(args)

    def subtract(self, a, b):
        return a - b

    def multiply(self, *args):
        # check whether all values are True (!0)
        if not all(args):
            raise ValueError
        return reduce(lambda x, y: x*y, args)

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return float('inf')

    def avg(self, it, upper_treshold=None, lower_treshold=None):
        if not lower_treshold:
            lower_treshold = min(it)

        if not upper_treshold:
            upper_treshold = max(it)

        # keep all elements that are less than or equal to the upper treshold
        _it = [x for x in it if x >= lower_treshold and x <= upper_treshold]

        if not len(_it):
            return 0

        return sum(_it) / len(_it)
