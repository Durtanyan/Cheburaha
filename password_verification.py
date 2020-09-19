# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 07:55:33 2020

@author: lukin
"""

password = input('Enter the password: ')

try:
    password[0]
    password.isdigit() / password.isalpha()
    int(password)
except IndexError:
    print('Empty string!')
except ZeroDivisionError:
    print('Your password consists only of numbers.')
except:
    print('Password requirements are met.')

    
    
    
    
    