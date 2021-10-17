# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 12:29:00 2021

@author: rikushwa
"""

'''
Exercise 3: Generate 6 digit random secure OTP
Reference article for help:

Python secrets module to generate secure numbers
Python get a random number within a range
'''

import secrets

secrets_generators = secrets.SystemRandom()
otp = secrets_generators.randrange(100000,999999)
print(otp)