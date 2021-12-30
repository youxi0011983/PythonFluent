#!/usr/bin/python
# -*- coding:UTF-8 -*-

import time
from clockdeco_param import clock


@clock('{name}: {elapsed}s')
def snooze(seconds):
    time.sleep(seconds)


if __name__ == '__main__':
    for i in range(5):
        snooze(.123)
