#!/usr/bin/python
# -*- coding:UTF-8 -*-

class StrKeyDict0(dict): # StrKeyDict0 继承了dict
    def __missing__(self, key):
        if isinstance(key, str): #如果找不到键本身就是字符串，那就抛出keyerror异常
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()
