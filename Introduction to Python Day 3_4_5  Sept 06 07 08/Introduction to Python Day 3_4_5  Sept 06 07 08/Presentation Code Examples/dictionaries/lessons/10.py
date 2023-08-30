#!/usr/bin/env python3

contacts = {'Jason': '555-0123', 'Carl': '555-0987'}
for person, phone_number in contacts.items():
    print('The number for {0} is {1}.'.format(person, phone_number))
