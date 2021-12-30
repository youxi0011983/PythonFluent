#!/usr/bin/python
# -*- coding:UTF-8 -*-
import time
from clockdeco import clock


@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    start = time.time()
    print(fibonacci(20))
    spend = time.time() - start
    print("time is %s" % spend)
