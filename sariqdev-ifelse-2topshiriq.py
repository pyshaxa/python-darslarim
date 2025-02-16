# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 17:50:18 2025

@author: User
"""

ism = input("Ismingizni kiriting>>>")
if ism.lower()=='admin':
    print(f"Xush kelibsiz {ism.title()}!")
    print("Foydalanuvchilar ro'yxatini ko'rasizmi?") 
else:
    print(f"Xush kelibsiz {ism.upper()}!!!")