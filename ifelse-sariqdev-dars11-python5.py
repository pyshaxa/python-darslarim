# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 10:10:16 2025

@author: User
"""

foydalanuvchilar=['umar',"shaxriyor",'ali','nizom','azim']
a=str(input("Yangi kirit"))
if a.lower() in foydalanuvchilar:
    print("Login band, yangi login kiriting!!!")
else:
    print(f"Xush kelibsiz {a.title()}!!!")