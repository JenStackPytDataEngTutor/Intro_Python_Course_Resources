#!/usr/bin/env python3


def high_and_low(numbers):
    """Determine the highest and lowest number"""
    highest = max(numbers)
    lowest = min(numbers)
    return (highest, lowest)

lottery_numbers = [16, 4, 42, 15, 23, 8]
(highest, lowest) = high_and_low(lottery_numbers)
print('The highest number is: {}'.format(highest))
print('The lowest number is: {}'.format(lowest))
