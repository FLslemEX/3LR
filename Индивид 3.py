#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    x = float(input("Сколько должен заплатить клиент в кассу? "))
    if x>500:
        q=x//500
        w=(x-q*500)//100
        e=(x-q*500-w*100)//10
        r=(x-q*500-w*100-e*10)//5
        t=(x-q*500-w*100-e*10-r*5)//2
        y=(x-q*500-w*100-e*10-r*5-t*2)//1
        a=q+w+e+r+t+y
        print(f"купюр он отдаст - {a}")
    elif 500>x:
        w = x // 100
        e = (x - w * 100) // 10
        r = (x - w * 100 - e * 10) // 5
        t = (x - w * 100 - e * 10 - r * 5) // 2
        y = (x - w * 100 - e * 10 - r * 5 - t * 2) // 1
        a = w + e + r + t + y
        print(f"купюр он отдаст - {a}")
    elif 100>x:
        e = x // 10
        r = (x - w * 100 - e * 10) // 5
        t = (x - w * 100 - e * 10 - r * 5) // 2
        y = (x - w * 100 - e * 10 - r * 5 - t * 2) // 1
        a = e + r + t + y
        print(f"купюр он отдаст - {a}")
    elif 10>x:
        r = x // 5
        t = (x - r * 5) // 2
        y = (x - r * 5 - t * 2) // 1
        a = r + t + y
        print(f"купюр он отдаст - {a}")
    elif 5>x:
        t = x // 2
        y = (x - t * 2) // 1
        a = t + y
        print(f"купюр он отдаст - {a}")
    elif 2>x:
        y = x // 1
        a = y
        print(f"купюр он отдаст - {a}")