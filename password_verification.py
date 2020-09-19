# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 07:55:33 2020

@author: lukin
"""

password = input('Enter the password: ')
indicator = '1'


try:
    a = password.isalpha()/ len(password)
    a = int(password) + (indicator)
except ZeroDivisionError:
    print('Empty string!')
except TypeError:
    print('Your password consists only of numbers.')
except:
    print('Password requirements are met.')

    
    
    
    
    