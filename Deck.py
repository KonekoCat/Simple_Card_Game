# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 01:15:40 2022

@author: KonekoCat

Class: Deck

Deck's class

"""
import random
import Card

class Deck():
    def __init__(self):
        self.__amount = 0
        self.__card_list = list()
        self.__top_index = 0
    
    def ready_new_deck(self, _shuffled = True):
        self.__card_list = [Card(i, j) for i in range(4) 
                                       for j in range(13)]
        if _shuffled:
            random.shuffle(self.__card_list)
        self.__amount = 52
        self.__top_index = 0
    
    def send_card(self) -> Card:
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
    
    