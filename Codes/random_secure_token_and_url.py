# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:22:59 2021

@author: rikushwa
"""

'''
Exercise 8: Generate random secure token of 64 bytes and random URL
'''

import secrets

print("Random secure Hexadecimal token is ", secrets.token_bytes(64))
print("Random secure URL is ", secrets.token_urlsafe(64))