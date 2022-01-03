#!/usr/bin/python
# -*- coding:UTF-8 -*-

class TwilightBus:
    """让乘客销声匿迹的校车"""
    
    def __init__(self,passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            # self.passengers = passengers  传递了别名会导致员列表被改变
            self.passengers = list(passengers)
    
    def pick(self,name):
        self.passengers.append(name)
        
    def drop(self,name):
        self.passengers.remove(name)