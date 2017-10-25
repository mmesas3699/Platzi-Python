# -*- coding: utf-8 -*-


for i in range(30):
    if i % 3 != 0:
        continue
    else:
        print(i)
        print(i**2)


for i in range(30):
    if i % 3 == 0:
        print(i)
    elif i == 22:
        break
