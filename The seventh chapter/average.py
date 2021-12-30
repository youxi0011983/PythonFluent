#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 平均值的函数实现

def make_averager():
    serise = []

    def averager(new_value):
        serise.append(new_value)
        total = sum(serise)
        return total / len(serise)

    return averager


if __name__ == '__main__':
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))
