#!/usr/bin/python
# -*- coding:UTF-8 -*-
# clockdeco_demo.py

import time
from clockdeco2 import clock


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    '6! =', factorial(6)
