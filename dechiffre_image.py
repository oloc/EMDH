#!/usr/bin/env python
# -*-coding:UTF-8 -*
#
# Olivier Locard

from PIL import Image

img = Image.open(input("Quelle image voulez-vous déchiffrer ?\n"))

width, height = img.size
pixels = img.load()

for x in range(width):
    for y in range(height):
        (r, g, b, a) = pixels[x, y]
        pixels[x, y] = (r * 10, 0, 0, a)

img.show()