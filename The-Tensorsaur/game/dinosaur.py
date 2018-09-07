import pyglet
'''
Created on Sep 7, 2018

@author: 17cha
'''
#Dino Class
class Dinosaur:
    def __init__(self):
        time = 0
    def createSprite (self):
        imageArray = [pyglet.image.load('sprites/dinoRightUp.png'), pyglet.image.load('sprites/dinoLeftUp.png')]
        animation = pyglet.image.Animation.from_image_sequence(imageArray, .1, True)
        bin = pyglet.image.atlas.TextureBin()
        animation.add_to_texture_bin(bin)
        return pyglet.sprite.Sprite(img=animation)
#End of Class