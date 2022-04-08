# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 01:15:40 2022

@author: KonekoCat

Class: Deck

Deck's class
Have 52 Cards in list.

"""
import random
from Card import Card

class Deck():
    MAX_AMOUNT = 52
    
    # Constructor
    def __init__(self):
        self.__amount = 0
        self.__card_list = list()
        self.__top_index = 0
    
    def ready_new_deck(self, _shuffled = True):
        self.__card_list.extend([Card(i, j) for i in range(4) \
                                            for j in range(1, 14)])
        if _shuffled:
            random.shuffle(self.__card_list)
        self.__amount = 52
        self.__top_index = 0
    
    def send_card(self) -> Card:
        if self.__top_index >= Deck.MAX_AMOUNT:
            raise IndexError("Deck havn\'t over 52 cards.")
        send_card = self.__card_list[self.__top_index]
        self.__top_index += 1
        return send_card
    
    def send_cards(self, _amount: int) -> list:
        send_list = list()
        for i in range(_amount):
            send_list.append(self.send_card())
        return send_list
    
    def check_top(self) -> Card:
        return self.__card_list[self.__top_index]

    @property
    def amount(self) -> int:
        return self.__amount


# confirm class
# check all methods
def main():
    deck = Deck()
    deck.ready_new_deck()
    
    c_list = list()
    card = deck.check_top()
    print(card.look())
    c_list = deck.send_cards(5)
    c_list.extend([deck.send_card() for i in range(Deck.MAX_AMOUNT - 5)])
    print([card.look() for card in c_list])
    
if __name__ == "__main__":
    main()

