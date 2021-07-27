#!/usr/bin/env python
# -*-coding:UTF-8 -*
#
# Olivier Locard

from random import randint

from PIL import Image

img = Image.open(input("Quelle image voulez-vous chiffrer ?\n"))

width, height = img.size
pixels = img.load()

for x in range(width):
    for y in range(height):
        (r, g, b, a) = pixels[x, y]
        pixels[x, y] = (int(r / 10), randint(0, 255), randint(0, 255))

img.save("oloc.png")
