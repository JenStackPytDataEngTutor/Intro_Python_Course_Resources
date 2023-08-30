#!/usr/bin/env python3

days_of_the_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
monday = days_of_the_week[0]
print(monday)
print()

for day in days_of_the_week:
    print(day)

# You cannot modify values in a tuple.  This will raise an exception.
days_of_the_week[0] = 'New Monday'
