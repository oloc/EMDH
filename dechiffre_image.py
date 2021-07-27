#!/usr/bin/env python
# -*-coding:UTF-8 -*
#
# Olivier Locard

from PIL import Image

image_name = input("Quelle image voulez-vous déchiffrer ?\n")
image_ext = image_name[-4:].lower()
img = Image.open(image_name)

width, height = img.size
pixels = img.load()

for x in range(width):
    for y in range(height):
        if image_ext == '.png':
            (r, g, b, a) = pixels[x, y]
        elif image_ext == '.jpg':
            (r, g, b) = pixels[x, y]
        pixels[x, y] = (r * 10, 0, 0)

img.show()
