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
    
    def draw_card(self, deck: Deck):
        self.__card_list.append(deck.send_card())
        self.__card_count += 1
    
    def select_card(self):
        self.__select_index = int(input("Which one select?")) - 1
        while not 0 <= self.__select_index <= self.__card_count - 1:
            self.__select_index = int(input("Select again:")) - 1
            
    def send_card(self) -> Card:
        pass
        
        