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
    
    # Constructor
    # suit = -1 is the initalize value
    def __init__(self, _suit: int = -1, _value: int = -1):
        if not (-1 <= _suit <= 3):
            raise ValueError("Card suit not in 0 ~ 3.")
        elif not (1 <= _value <= 13 or _value == -1):
            raise ValueError("Card value not in 1 ~ 13(A ~ K).")
            
        self.__suit = _suit
        self.__value = _value
    
    def look(self) -> str:
        if self.__suit == -1:
            s = "*"
        else:
            s = Card.__SUIT[self.__suit] + \
                Card.__VALUE[self.__value - 1]
        return s
    
    @property
    def suit(self) -> int:
        return self.__suit
    
    @property
    def value(self) -> int:
        if self.__suit == -1:
            raise ValueError("The card is closed.")
        return self.__value


# confirm class
# check all methods
def main():
    card = Card(0, 8)
    print(card.suit)
    print(card.value)
    print(card.look())

    c_list = list()
    c_list.append(Card(0, 8))
    print(c_list[0].look())

if __name__ == "__main__":
    main()



