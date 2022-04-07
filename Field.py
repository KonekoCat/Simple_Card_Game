# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 19:00:44 2022

@author: George Su
"""
import copy

import Card
import Deck
import Player

class Field():
    def __init__(self, _p_list: list, _deck: Deck):
        self.player_list = [i for i in _p_list.copy()]
        self.deck = copy.deepcopy(_deck)
    
    def update_player(self, player: Player, player_num: int):
        pass
    
    def update_deck(self, deck: Deck):
        pass
    
    def update_card(self, player_num: int):
        pass

    def show(self):
        pass





