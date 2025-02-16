# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 17:45:28 2025

@author: User
"""

moshinalar = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for moshin in moshinalar:
    if moshin != 'gm':
        print(moshin.title())
    else:
        print(moshin.upper())