# -*- coding: cp1250 -*-
a = "Cze��"
print(a)

with open('kodowanie.txt') as f:
    s = f.read()
print(s)

with open('kodowanie2.txt', encoding='utf-8') as f:
    s = f.read()
print(s)
