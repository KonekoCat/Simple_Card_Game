# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 00:45:44 2022

@author: KonekoCat

Class: Player

Player's class

"""
import Card
import Deck

class Player():
    def __init__(self, _name: str):
        self.__name = _name
        self.__winSet = 0
        self.__point = 0
        self.__card_list = list()
        self.__card_count = 0
        self.__select_index = -1    # No select
    
    def draw_card(self, _deck: Deck):
        self.__card_list.append(_deck.send_card())
        self.__card_count += 1
    
    def draw_cards(self, _deck: Deck, _amount: int):
        self.__card_list.extend(_deck.send_cards(_amount))
        self.__card_count += _amount
    
    def select_card(self):
        self.__select_index = int(input("Which one select?")) - 1
        while not 0 <= self.__select_index <= self.__card_count - 1:
            self.__select_index = int(input("Select again:")) - 1
            
    def send_card(self) -> Card:
        if self.__select_index != -1:
            send_card = self.__card_list.pop(self.__select_index)
            self.__card_count -= 1
            return send_card
        else:
            print("Select Invalid.")
        
    def drop_cards(self):
        self.__card_list.clear()
        self.__card_count = 0
        self.__select_index = -1
    
    def win_set(self):
        self.__winSet += 1
        self.__point = 0
    
    def lose_set(self):
        self.__point = 0
    
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def winSet(self) -> int:
        return self.__winSet
    
    @property
    def point(self) -> int:
        return self.__point