#!/usr/bin/python
# -*- coding:UTF-8 -*-

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

if __name__ == '__main__':
    for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
        print(tshirt)
