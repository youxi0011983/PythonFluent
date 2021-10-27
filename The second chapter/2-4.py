#!/usr/bin/python
# -*- coding:UTF-8 -*-

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print("tshirts", tshirts)

for color in colors:
    for size in sizes:
        print((color, size))

tshirts = [(color, size) for size in sizes for color in colors]
print("tshirts", tshirts)
