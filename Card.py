# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 14:30:49 2022

@author: KonekoCat

Class: Card

Trump's class Use
Suit: ♣♦♥♠
value: A2-10JQK
"""

class Card():
    __SUIT = dict(enumerate(['♣', '♦', '♥', '♠']))
    __VALUE = ['A'] + [str(i) for i in range(2, 11)] + list("JQK")
    
    def __init__(self, _suit: int, _value: int):
        self.__suit = _suit
        self.__value = _value
        
    
    def look(self) -> str:
        s = Card.__SUIT[self.__suit - 1] + \
            Card.__VALUE[self.__value - 1]
        return s


    @property
    def suit(self) -> int:
        return self.__suit
    
    @property
    def value(self) -> int:
        return self.__value


# confirm class
if __name__ == "__main__":
    card = Card(0, 8)
    card.suit = 2
    print(card.look())

