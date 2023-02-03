# -*- coding: utf-8 -*-

from functools import reduce


class SimpleCalculator:
    def add(self, *args):
        return sum(args)

    def subtract(self, a, b):
        return a - b

    def multiply(self, *args):
        def multiply2(a, b):
            return a * b

        return reduce(multiply2, args)
