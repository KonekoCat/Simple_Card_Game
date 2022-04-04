# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 14:30:49 2022

@author: George Su
"""

class Card():
    __SUIT = dict(enumerate(['♣', '♦', '♥', '♠']))
    __VALUE = ['A'] + [str(i) for i in range(2, 11)] + list("JQK")
    
    def __init__(self, _suit: int, _value: int):
        self.__suit = _suit
        self.__value = _value - 1
    
    def look(self) -> str:
        s = Card.__SUIT[self.__suit] + Card.__VALUE[self.__value]
        return s


    @property
    def suit(self) -> str:
        return Card.__SUIT[self.__suit]
    @suit.setter
    def suit(self, _suit):
        self.__suit = _suit
    
    @property
    def value(self) -> str:
        return Card.__VALUE[self.__value]
    @value.setter
    def value(self, _value):
        self.__value = _value - 1


# confirm class
if __name__ == "__main__":
    card = Card(0, 8)
    card.suit = 2
    print(card.look())

