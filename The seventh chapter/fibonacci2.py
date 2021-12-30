#!/usr/bin/python
# -*- coding:UTF-8 -*-
import time
import functools
from clockdeco import clock


@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    start = time.time()
    print(fibonacci(200))
    spend = time.time() - start
    print("time is %s" % spend)