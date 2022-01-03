#!/usr/bin/python
# -*- coding:UTF-8 -*-

if __name__ == '__main__':
    l1 = [3, [66, 55, 44], (7, 8, 9)]
    l2 = list(l1)
    l1.append(100)
    l1[1].remove(55)
    print('l1:', l1)
    print('l2:', l2)
    l2[1] += [33, 22]
    l2[2] += (10, 11) # +=对雨元组来说，相当于创建了一个新的元组。
    print('l1:', l1)
    print('l2:', l2)
