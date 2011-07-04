#!/usr/bin/python
#-*- coding:utf-8 -*-

"""
    ClassEuler: Pythonic solutions to Euler Project problems.
"""

class ClassEuler ():

    """
        Methods:
            twopow1000sum: Sum of digits of 2^1000
            sum_5_3: Sum of all multiples of 3 or 5 within specified limits.
            fibo: Fibonacci series generator
            fibolen1000: Returns first term of fibonacci series with 1000 digits.
            fibo_even_sum: Determines sum of even elements of a fibonacci series within a limit.
    """

    def __init__(self, ):
        pass

    @classmethod
    def twopow1000sum(cls):
        """
            ClassEuler:
                twopow1000sum:  Returns the sum of digits in 2^1000
        """
        return reduce(lambda x, y:(int(x)+int(y)), [x for x in str(2**1000)])

    @classmethod
    def sum_5_3(cls, ll, ul):
        """
        sum_5_3: Function to find the sum of all multiples of 3 or 5 between the limits specified. Usage: sum_5_3(<range_lower_limit>,<range_upper_limit>). Returns sum
        """
        a = [ x for x in range(ll, ul) if not x%3 or not x%5]
        return reduce(lambda f, s: (f+s), a)

    @classmethod
    def fgen(cls, lim):
        """
        fgen: Function to generate a fibonacci series with a user specified range. Usage: fgen(<upper_limit>). Returns the series as a list.
        """
        a, b, fl = 0, 1, []
        while b < lim:
            fl.append(b)
            a, b = b, a+b
        return fl

    @classmethod
    def fibolen1000(cls):
        """
        fibolen1000: Function to generate a fibonacci series and find the first term with 1000 digits. Usage: fgen().
        """
        a, b, fl = 0, 1, []
        while len(str(b))<=1000:
            fl.append(b)
            a, b = b, a+b
        return str(fl[len(fl)-1])

    def fibo_even_sum(self, lim):
        """
        fibo_even_sum: Function to determine the sum of even terms of a Fibonacci series within a specified limit. Usage: fibo_even_sum(<fibonacci_series_limit>)
        """
        a = [x for x in self.fgen(lim) if not x%2]
        return reduce(lambda f, s: (f+s), a)
