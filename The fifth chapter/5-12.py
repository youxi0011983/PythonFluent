#!/usr/bin/python
# # -*- coding:UTF-8 -*-
import bobo


@bobo.query('/')
def hello(person):
    return 'Hello %s!' % person
