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
