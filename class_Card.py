# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 14:30:49 2022

@author: George Su
"""

class Card():
    __SUIT = dict(enumerate(['♣', '♦', '♥', '♠']))
    __VALUE = ['A'] + [i for i in range(2, 11)] + list("JQK")
    
    def __init__(self, _suit: int, _value: int):
        self.__suit = _suit
        self.__value = _value

