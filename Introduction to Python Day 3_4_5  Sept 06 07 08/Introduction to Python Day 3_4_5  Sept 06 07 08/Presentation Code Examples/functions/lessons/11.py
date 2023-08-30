#!/usr/bin/env python3


def odd_or_even(number):
    """Determine if a number is odd or even."""
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

odd_or_even_string = odd_or_even(7)
print(odd_or_even_string)
