#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    z = float(input("Цена 1 рулона обоев? "))
    y = float(input("Цена 1 банки краски? "))
    o = float(input("Сколько куплено рулонов обоев? "))
    k = float(input("Сколько куплено банок краски? "))
    e=z*o
    r=y*k
    x=e+r
    if 200 < x < 500:
        a = x - x*3/100
        print(f"{a} рублей")
    elif 500 < x < 800:
        b = x - x*5/100
        print(f"{b} рублей")
    elif 800 < x < 1000:
        c = x - x*7/100
        print(f"{c} рублей")
    elif x > 1000:
        d = x - x*9/100
        print(f"{d} рублей")
