#!/usr/bin/env python3

contacts = {'Jason': '555-0123', 'Carl': '555-0987'}
contacts['Jason'] = '555-0000'
jasons_phone = contacts['Jason']
print('Dial {} to call Jason.'.format(jasons_phone))
