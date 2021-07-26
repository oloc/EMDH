#!/usr/bin/env python
# -*-coding:UTF-8 -*
#
# Olivier Locard

from random import randint

cards_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
colors_list = ['Carreau', 'Coeur', 'Pique', 'Trèfle']

print("Carte tirée au hasard : " + cards_list[randint(0, 12)] + " de " + colors_list[randint(0, 3)])
