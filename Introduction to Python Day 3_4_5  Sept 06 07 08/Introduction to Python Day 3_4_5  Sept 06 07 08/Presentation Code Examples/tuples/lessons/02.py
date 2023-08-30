#!/usr/bin/env python3

days_of_the_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
print(days_of_the_week)
del days_of_the_week
# This will raise an exception since the tuple was deleted.
print(days_of_the_week)
