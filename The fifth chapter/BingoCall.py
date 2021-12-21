#!/usr/bin/python
# # -*- coding:UTF-8 -*-
import random


class BingoCage:
    def __init__(self, items):
        self._items = list(items)  # 接受任务和迭代对象
        random.shuffle(self._items)

    def pick(self):  # 起主要作用的方法
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')  # 如果self._items为空，抛出异常。

    def __call__(self):
        return self.pick()
