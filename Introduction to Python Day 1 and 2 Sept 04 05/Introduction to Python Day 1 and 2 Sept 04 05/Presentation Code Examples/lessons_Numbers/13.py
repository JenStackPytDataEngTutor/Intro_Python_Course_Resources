#!/usr/bin/env python3

# Get the input from the user.
text = input('What would you like the cat to say? ')

# Determine the length of the input.
text_length = len(text)

# Make the border the same size as the input.
print('            {}'.format('_' * text_length))
print('          < {} >'.format(text))
print('            {}'.format('-' * text_length))
print('          /')
print(' /\_/\   /')
print('( o.o )')
print(' > ^ <')
