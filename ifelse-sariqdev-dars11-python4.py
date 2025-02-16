# -*- coding: utf-8 -*-
"""
Shaxriyor_py
"""

maxsulot=["klaviatura","sichqoncha","noutbuk","monitor","keys","kreslo","kuller","vebcamera","parta","telefon"]
bizda_bor=[]
bizda_yoq=[]
#print(len(maxsulot))
for i in range(5):
    d=input(f"Savatga {i+1}-maxsulotni kiriting: ")
    if d in maxsulot:
        bizda_bor.append(d)
    else:
        bizda_yoq.append(d)
if bizda_yoq:
    for yoq in bizda_yoq:
        print(f"Bizda {yoq} yo'q ekan.")
else:
    print("Bizda siz so'ragan hamma narsa bor.")