# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 19:00:44 2022

@author: George Su
"""
import copy

from Card import Card
from Deck import Deck
from Player import Player

class Field():
    # Constructor
    def __init__(self, _p_list: list, _deck: Deck):
        self.player_list = [i for i in _p_list.copy()]
        self.deck = copy.deepcopy(_deck)
        self.field_card = [Card() for i in range(2)]
    
    def update_player(self, _player: Player, _player_num: int):
        self.player_list[_player_num] = copy.deepcopy(_player)
    
    def update_deck(self, _deck: Deck):
        self.deck = copy.deepcopy(_deck)
    
    def update_card(self, _card: Card, _player_num: int):
        self.field_card[_player_num] = copy.deepcopy(_card)

    def show(self):
        print("-" * 52)
        infoLine = "|{:^50}|\n" +\
                   "|{:<25}{:>25}|\n" +\
                   "|{:^50}|\n" +\
                   "|" + " " * 50 + "|\n" +\
                   "|{:^50}|\n" +\
                   "|{:<25}{:>25}|\n" +\
                   "|{:^50}|"           
        cpuCard = " ".join([card.look() \
                              for card in self.player_list[1].card_info()])
        playerCard = " ".join([card.look() \
                                 for card in self.player_list[0].card_info()])

        print(infoLine.format("{}".format(cpuCard), 
                              "win set: " + str(self.player_list[1].winSet), 
                              "point: " + str(self.player_list[1].point), 
                              "{}".format(self.player_list[1].show_card().look()), 
                              "{}".format(self.player_list[0].show_card().look()), 
                              "win set: " + str(self.player_list[0].winSet), 
                              "point: " + str(self.player_list[0].point), 
                              "{}".format(playerCard)))
        print("-" * 52)
        
        
# confirm class
# check all methods 
def main():
    player1 = Player("Self")
    player2 = Player("CPU")
    player_list = [player1, player2]
    
    deck = Deck()
    deck.ready_new_deck()
    player_list[0].draw_cards(deck, 5)
    player_list[1].draw_cards(deck, 5)
    
    field = Field(player_list, deck)
    field.show()
    
    
if __name__ == "__main__":
    main()

