#!/usr/bin/python
# -*- coding:UTF-8 -*-

import unicodedata
import string


def shave_marks(txt):
    """去掉全部变音符号"""
    norm_txt = unicodedata.normalize('NFD', txt)  # 把所有的字符分解为基字符和组合记号
    shaved = ''.join(c for c in norm_txt
                     if not unicodedata.combining(c))  # 过滤掉所有的组合记号
    return unicodedata.normalize('NFC', shaved)  # 重组所有字符


def shave_marks_latin(txt):
    """把拉丁基字符中所有的变音符号删除"""
    norm_txt = unicodedata.normalize('NFD', txt)
    latin_base = False
    keepers = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:
            continue  # 忽略拉丁基字符上的变音符号
        keepers.append(c)
        # 如果不是组合字符，那就是新的基字符
        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters
    shaved = ''.join(keepers)
    return unicodedata.normalize('NFC', shaved)


