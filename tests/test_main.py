#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simple_calculator.main import SimpleCalculator


def test_add_two_numbers():
    calculator = SimpleCalculator()

    result = calculator.add(4, 5)

    assert result == 9


def test_add_three_numbers():
    calculator = SimpleCalculator()

    result = calculator.add(4, 5, 6)

    assert result == 15


def test_add_many_numbers():
    numbers = range(100)

    calculator = SimpleCalculator()

    result = calculator.add(*numbers)

    # 4950 is the sum of all numbers from 0 to 99
    assert result == 4950


def test_subtract_two_numbers():
    calculator = SimpleCalculator()

    result = calculator.subtract(10, 3)

    assert result == 7

def test_multiply_two_numbers():
    calculator = SimpleCalculator()

    result = calculator.multiply(6, 4)

    assert result == 24

def test_multiply_many_numbers():
    numbers = range(1, 10)

    calculator = SimpleCalculator()

    result = calculator.multiply(*numbers)

    assert result == 362880

def test_divide_two_numbers_float():
    calculator = SimpleCalculator()

    result = calculator.divide(13, 2)

    assert result == 6.5
