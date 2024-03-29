# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 00:45:44 2022

@author: KonekoCat

Class: Player

Player's class

"""
from Card import Card
from Deck import Deck

class Player():
    # Constructor
    def __init__(self, _name: str):
        self.__name = _name
        self.__win_set = 0
        self.__point = 0
        self.__card_list = list()
        self.__cardCount = 0
        self.__select_index = -1    # No select
    
    def draw_card(self, _deck: Deck):
        self.__card_list.append(_deck.send_card())
        self.__cardCount += 1
    
    def draw_cards(self, _deck: Deck, _amount: int):
        self.__card_list.extend(_deck.send_cards(_amount))
        self.__cardCount += _amount
    
    def select_card(self):
        self.__select_index = int(input("Which one select?")) - 1
        while not 0 <= self.__select_index <= self.__card_count - 1:
            self.__select_index = int(input("Select again:")) - 1
    
    def show_card(self) -> Card:
        if self.__select_index != -1:
            send_card = self.__card_list[self.__select_index]
            self.__cardCount -= 1
            return send_card
        else:
            return Card()
            
    def send_card(self) -> Card:
        if self.__select_index != -1:
            send_card = self.__card_list.pop(self.__select_index)
            self.__cardCount -= 1
            return send_card
        else:
            return Card()
    
    def card_info(self) -> list:
        return self.__card_list
        
    def drop_cards(self):
        self.__card_list.clear()
        self.__cardCount = 0
        self.__select_index = -1
    
    def win_set(self):
        self.__win_set += 1
        self.__point = 0
    
    def lose_set(self):
        self.__point = 0
    
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def winSet(self) -> int:
        return self.__win_set
    
    @property
    def point(self) -> int:
        return self.__point
    
    @property
    def cardCount(self) -> int:
        return self.__cardCount
    
# confirm class
# check all methods 
def main():
    name = "test"
    player = Player(name)
    
    
if __name__ == "__main__":
    main()

