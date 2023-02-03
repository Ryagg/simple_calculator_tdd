# -*- coding: utf-8 -*-

from functools import reduce


class SimpleCalculator:
    def add(self, *args):
        return sum(args)

    def subtract(self, a, b):
        return a - b

    def multiply(self, *args):
        return reduce(lambda x, y: x*y, args)

    def divide(self, a, b):
        return a / b
